import sys
import os, time, socket, select
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap, QIcon,QFont,QCursor
from PyQt5.QtWidgets import QGraphicsScene,QGraphicsPixmapItem
from PyQt5.QtCore import Qt, QTimer  # Import Qt for alignment
from .layouts.gauge import Gauge
from .layouts import ui_wireless
import numpy as np
import pyqtgraph as pg


class Expt(QtWidgets.QWidget, ui_wireless.Ui_Form):
    def __init__(self, device, **kwargs):
        super().__init__()
        self.setupUi(self)
        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(False)
        self.SENDPORT=12345
        self.CONFIGPORT=5555
        self.SHOWUP = 101

        # Create a UDP socket for listening to broadcasts
        self.bsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bsock.setblocking(False)
        self.BCASTPORT=9999

        self.sock.bind(('0.0.0.0', self.SENDPORT))
        self.bsock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.bsock.bind(('0.0.0.0', self.BCASTPORT))

        # Prepare for plotting
        self.plot = self.plotLayout.addPlot(title="Acceleration")
        self.plot.setLabel('left', 'Acceleration (m/s^2)')
        self.plot.setLabel('bottom', 'Time (s)')
        self.curve_x = self.plot.plot(pen='y', name='Ax')
        self.curve_y = self.plot.plot(pen='r', name='Ay')
        self.curve_z = self.plot.plot(pen='g', name='Az')

        self.curve_gx = pg.PlotCurveItem(pen=pg.mkPen(color='cyan', width=1))
        self.curve_gy = pg.PlotCurveItem(pen=pg.mkPen(color='magenta', width=1))
        self.curve_gz = pg.PlotCurveItem(pen=pg.mkPen(color='white', width=1))
        self.combinedPlot = False

        if self.combinedPlot:
            ## create a new ViewBox, link the right axis to its coordinate system
            self.p2 = pg.ViewBox()
            self.plot.showAxis('right')
            self.plot.scene().addItem(self.p2)
            self.plot.getAxis('right').linkToView(self.p2)
            self.p2.setXLink(self.plot)
            self.plot.setLabel('right', 'Gyro', units="<font>&omega;</font>",
                        color='#025b94', **{'font-size':'14pt'})
            self.plot.getAxis('right').setPen(pg.mkPen(color='magenta', width=2))

            self.p2.addItem(self.curve_gx)
            self.p2.addItem(self.curve_gy)
            self.p2.addItem(self.curve_gz)

            self.updateViews()
            self.plot.vb.sigResized.connect(self.updateViews)
        else:
            self.plotLayout.nextRow()
            self.gyroplot = self.plotLayout.addPlot(title="Angular Velocity")
            self.gyroplot.setLabel('left', 'Angular Velocity (rad/s)')
            self.gyroplot.setLabel('bottom', 'Time (s)')
            self.gyroplot.addItem(self.curve_gx)
            self.gyroplot.addItem(self.curve_gy)
            self.gyroplot.addItem(self.curve_gz)

        self.gauge_widgets = []
        r=0;c=0;
        self.ar = 16
        self.gr = 4.5
        for a in ['Ax','Ay','Az','Gx','Gy','Gz']:
            self.gauge_widget = Gauge(self, a)
            self.gauge_widget.setObjectName(a)
            self.gauge_widget.set_MinValue(-1*self.ar)
            self.gauge_widget.set_MaxValue(self.ar)
            self.gauge_widget.setMinimumWidth(50)
            self.gaugeLayout.addWidget(self.gauge_widget, r, c)
            self.gauge_widgets.append(self.gauge_widget)
            if c==1:
                self.gauge_widget.set_MinValue(-1*self.gr)
                self.gauge_widget.set_MaxValue(self.gr)

            r+=1
            if r==3:
                r=0
                c+=1

        self.g_offsets=None
        self.g_avgs = np.zeros([50,3])
        self.g_avg_points=-1

        self.NP = 2000
        self.data = np.full((self.NP, 7), np.nan)  # Store timestamp, x, y, z filled with NaN
        self.ptr = 0
        self.first_time = None
        #self.addr = ['10.42.0.16',self.CONFIGPORT]
        self.addr = None
        self.splitter.setSizes([1,4])

        self.graph_updated = time.time()
        # Set up a timer to read UDP data
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_udp_data)
        #self.timer.start(200)  # Check for data every 2 ms

        self.btimer = QTimer(self)
        self.btimer.timeout.connect(self.read_bcast_data)
        self.btimer.start(50)  # Check for broadcast data every x mS

    ## Handle view resizing 
    def updateViews(self):
        self.p2.setGeometry(self.plot.vb.sceneBoundingRect())
        self.p2.linkedViewChanged(self.plot.vb, self.p2.XAxis)

    def read_bcast_data(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(chr(self.SHOWUP).encode(), ("255.255.255.255", self.CONFIGPORT))

        if select.select([self.bsock],[],[],0.1)[0]:
            dat, addr = self.bsock.recvfrom(10)
            print(dat, addr)
            if dat == b'CSPark_IMU':
                print('sensor available', dat)
                self.addr = addr
                self.statusLabel.setText(f'Sensor {dat.decode()} found at {addr[0]}. Start Measurements now.')
                self.statusLabel.setStyleSheet('color:green;')
                self.btimer.stop()
                self.controlsFrame.setEnabled(True)

    def crc32(self,data: bytes, polynomial: int = 0x04C11DB7, initial_crc: int = 0xFFFFFFFF, final_xor: int = 0xFFFFFFFF, reflect_input: bool = True, reflect_output: bool = True) -> int:
        """
        Calculate the CRC-32 checksum.

        Args:
            data (bytes): Input data as a bytes object.
            polynomial (int): CRC-32 polynomial (default is 0x04C11DB7).
            initial_crc (int): Initial CRC value (default is 0xFFFFFFFF).
            final_xor (int): Value to XOR with final CRC (default is 0xFFFFFFFF).
            reflect_input (bool): Whether to reflect input bytes.
            reflect_output (bool): Whether to reflect the final CRC value.

        Returns:
            int: Calculated CRC-32 value.
        """

        def reflect_bits(value: int, num_bits: int) -> int:
            """Reflect the `num_bits` least significant bits of `value`."""
            reflection = 0
            for _ in range(num_bits):
                reflection = (reflection << 1) | (value & 1)
                value >>= 1
            return reflection

        # Initialize CRC
        crc = initial_crc

        # Process each byte in the data
        for byte in data:
            if reflect_input:
                byte = reflect_bits(byte, 8)
            crc ^= (byte << 24)
            for _ in range(8):  # Process each bit in the byte
                if crc & 0x80000000:
                    crc = (crc << 1) ^ polynomial
                else:
                    crc <<= 1
                crc &= 0xFFFFFFFF  # Keep CRC 32-bit

        # Final reflection and XOR
        if reflect_output:
            crc = reflect_bits(crc, 32)
        return crc ^ final_xor

    def read_udp_data(self):
        # Receive data
        NB = 32
        if not select.select([self.sock],[],[],0.1)[0]:
            return
        dat, self.addr = self.sock.recvfrom(NB)  # Buffer size is 28+1 bytes
        if len(dat) == NB:
            timestamp, x, y, z, gx, gy, gz, crc = np.frombuffer(dat, dtype=[('timestamp', 'u4'), ('x', 'f4'), ('y', 'f4'), ('z', 'f4'), ('gx', 'f4'), ('gy', 'f4'), ('gz', 'f4'), ('crc', np.uint32)])[0]
            timestamp = timestamp * 1e-3 # convert to seconds
            if self.crc32(dat[:NB-4]) != crc:
                print("CRC mismatch")
                return

            if self.g_offsets is not None:
                gx -= self.g_offsets[0]
                gy -= self.g_offsets[1]
                gz -= self.g_offsets[2]
            elif self.g_avg_points>0:
                self.g_avgs[self.g_avg_points-1] = [gx,gy,gz]
                self.g_avg_points -= 1
            elif self.g_avg_points==0:
                self.g_offsets = np.zeros([3])
                self.g_offsets[0] = np.average(self.g_avgs[:,0])
                self.g_offsets[1] = np.average(self.g_avgs[:,1])
                self.g_offsets[2] = np.average(self.g_avgs[:,2])
                self.g_avg_points = -1

            if self.first_time is None:
                self.first_time = timestamp
            self.data[:-1] = self.data[1:]
            # Update plot data
            self.data[-1] = [timestamp-self.first_time, x, y, z, gx, gy, gz]
            self.ptr += 1

            if time.time() - self.graph_updated>0.03: # S
                self.gauge_widgets[0].update_value(x)
                self.gauge_widgets[1].update_value(y)
                self.gauge_widgets[2].update_value(z)
                self.gauge_widgets[3].update_value(gx)
                self.gauge_widgets[4].update_value(gy)
                self.gauge_widgets[5].update_value(gz)
                # Prevent connecting the last point to the first point
                self.curve_x.setData(self.data[:, 0], self.data[:, 1])
                self.curve_y.setData(self.data[:, 0], self.data[:, 2])
                self.curve_z.setData(self.data[:, 0], self.data[:, 3])
                self.curve_gx.setData(self.data[:, 0], self.data[:, 4])
                self.curve_gy.setData(self.data[:, 0], self.data[:, 5])
                self.curve_gz.setData(self.data[:, 0], self.data[:, 6])
                self.graph_updated = time.time()

            if self.ptr%1000==0:
                print(self.ptr,timestamp-self.first_time)

    def setAccelRange(self,r):
        if self.addr is not None:
            self.sock.sendto(chr(10+r).encode(), (self.addr[0], self.CONFIGPORT))  # Set accelerometer range
        mr = [20,40,80,160]
        for a in range(3):
            self.gauge_widgets[a].set_MinValue(-1*mr[r])
            self.gauge_widgets[a].set_MaxValue(mr[r])
        self.plot.setYRange(-1*mr[r],mr[r])

    def setGyroRange(self,r):
        if self.addr is not None:
            self.sock.sendto(chr(20+r).encode(), (self.addr[0], self.CONFIGPORT))  # Set accelerometer range
        mr = [4,8,16,32]
        for a in range(3):
            self.gauge_widgets[a+3].set_MinValue(-1*mr[r])
            self.gauge_widgets[a+3].set_MaxValue(mr[r])
        try:
            self.gyroplot.setYRange(-1*mr[r],mr[r])
        except:
            self.p2.setYRange(-1*mr[r],mr[r])

    def setFilter(self,r):
        if self.addr is not None:
            self.sock.sendto(chr(30+r).encode(), (self.addr[0], self.CONFIGPORT))  # Set filter frequency

    def offsetZero(self):
        reply = QtWidgets.QMessageBox.question(self, 'Correct Gyro Offset', "Place the device flat and free from any vibrations first.\ndone?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.g_offsets=None
            self.g_avg_points=40
            self.g_avgs = np.zeros([self.g_avg_points,3])


    def startCounter(self):
        print(self.addr)
        if self.addr is not None:
            self.sock.sendto(b'\x01', (self.addr[0], self.CONFIGPORT))  # Send start signal
            self.first_time = None
            self.data = np.full((self.NP, 7), np.nan)
            try:
                while True:
                    self.sock.recv(1024)
            except Exception as e:
                pass
            self.timer.start(2)

    def pauseCounter(self):
        if self.addr is not None:
            self.sock.sendto(b'\x00', (self.addr[0], self.CONFIGPORT))  # Send pause signal
            self.timer.stop()

    def reboot(self):
        self.timer.stop()
        self.btimer.stop()

        self.sock.sendto(chr(100).encode(), (self.addr[0], self.CONFIGPORT))  # Send reboot signal
        self.addr = None
        while select.select([self.bsock],[],[],0.1)[0]:
            dat, addr = self.bsock.recvfrom(9)

        self.statusLabel.setText(f'Rebooted hardware. Restart app as well...')
        self.statusLabel.setStyleSheet('color:red;')
        self.controlsFrame.setEnabled(False);
        self.btimer.start(200)

    def setWiFi(self):
        print(self.ipEdit.text(),self.pwdEdit.text())
        if self.addr is not None:
            self.sock.sendto(chr(50).encode() + f'{self.ipEdit.text()}\n{self.pwdEdit.text()}\n'.encode(), (self.addr[0], self.CONFIGPORT))  # Send wifi creds


# This section is necessary for running new.py as a standalone program

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Expt(None)  # Pass None for the device in standalone mode
    window.show()
    sys.exit(app.exec_()) 