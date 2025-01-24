"""
CivilPy
Copyright (C) 2019 - Dane Parks

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
# Dependency imports
from dataclasses import dataclass
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

# Package specific imports
from diagram import AbstractDiagramElement


@dataclass()
class PointLoad:

    nodeID = None

    def __init__(self, P, x, nodeID=None, label=''):
        self.P = P
        self.x = x
        self.nodeID = nodeID
        self.label = label
        self.loadPattern = None

    def _setID(self, newID):
        self.nodeID = newID

    def getPosition(self):
        return self.x


@dataclass()
class EleLoadDist:

    def __init__(self, x1: float, x2: float, distLoad: list, label: str = ''):
        self.x1 = x1
        self.x2 = x2
        self.P = distLoad
        self.label = label


@dataclass()
class EleLoadLinear:

    def __init__(self, x1: float, x2: float, linLoad: list, label: str = ''):

        self.x1 = x1
        self.x2 = x2
        self.P = linLoad
        self.label = label
        self.Lnet = x2 - x1

    def checkInRange(self, s):


        if s < self.x1:
            raise Exception(r'First point range, must be greater than {x1}')

        if self.x2 < s:
            raise Exception(r'Second point range, must be less than {self.x2}')

    def getLoadComponents(self, s1, s2, q):

        self.checkInRange(s1)
        self.checkInRange(s2)
        s1 = (s1 - self.x1) / self.Lnet
        s2 = (s2 - self.x1) / self.Lnet

        m = q[1] - q[0]

        y1 = s1 * m + q[0]
        y2 = s2 * m + q[0]

        return y1, y2


@dataclass
class PointLoadOptions:
    # GlobalParameters
    lw: float
    c: float  # colour
    arrowWidth: float


@dataclass
class DistLoadOptions:
    # GlobalParameters
    baseWidth: float
    c: float  # colour
    arrowWidth: float

    spacing: float
    barWidth: float


@dataclass
class LinLoadOptions:
    # GlobalParameters
    baseWidth: float
    c: float  # colour
    arrowWidth: float

    spacing: float
    barWidth: float
    minLengthCutoff: float


@dataclass
class MomentPointLoadOptions:
    # GlobalParameters
    lw: float
    c: float  # colour
    arrowWidth: float

    # Circle parameters
    r: float
    rotationAngle: float


class DiagramElePointLoad(AbstractDiagramElement):
    def __init__(self, xy0, dxy0, options: PointLoadOptions):
        self.xy0 = xy0
        self.dxy0 = dxy0
        self.width = options.lw
        self.arrowWidth = options.arrowWidth
        self.c = options.c

    def plot(self, ax):

        x, y = self.xy0
        Px, Py = self.dxy0
        c = self.c

        width = self.width
        hwidth = self.arrowWidth
        length = self.arrowWidth
        ax.arrow(x, y, Px, Py, width=width, head_width=hwidth,
                 head_length=length, edgecolor='none',
                 length_includes_head=True, fc=c)


class DiagramEleLoadDistributed(AbstractDiagramElement):
    def __init__(self, loadBox, diagramOptions: DistLoadOptions,
                 plOptions: PointLoadOptions):
        self.loadBox = loadBox
        # self.pointUp = loadBox.pointUp
        self.options = diagramOptions
        self.plOptions = plOptions
        self.minNbar = 3

    def plot(self, ax):

        barWidth = self.options.barWidth
        spacing = self.options.spacing
        barC = self.options.c
        x1, x2 = self.loadBox.x
        y1, y2 = self.loadBox.y

        N = max(int((x2 - x1) / spacing) + 1, self.minNbar)
        xVals = np.linspace(x1, x2, N)

        ystart = self.loadBox.fout[0]
        yend = self.loadBox.datum
        dy = ystart - yend

        xbar = [x1, x2]
        yBarS = [ystart, ystart]
        yBarE = [yend, yend]
        plt.plot(xbar, yBarS, linewidth=barWidth, c=barC)
        plt.plot(xbar, yBarE, linewidth=barWidth, c=barC)

        for ii in range(N):
            x = xVals[ii]
            # pointLoad = DiagramElePointLoad((x, ystart), (0, yend), self.plOptions)
            pointLoad = DiagramElePointLoad((x, ystart), (0, -dy), self.plOptions)
            pointLoad.plot(ax)


class DiagramEleLoadLinear(AbstractDiagramElement):

    def __init__(self, loadBox, diagramOptions: LinLoadOptions,
                 plOptions: PointLoadOptions):
        self.loadBox = loadBox
        self.options = diagramOptions
        self.plOptions = plOptions
        self.minNbar = 3

    def plot(self, ax):


        barWidth = self.options.barWidth
        minLengthCutoff = self.options.minLengthCutoff
        spacing = self.options.spacing
        barC = self.options.c
        x1, x2 = self.loadBox.x
        # y1, y2 = self.loadBox.y

        # baseLineWidth = 0.015

        Nlines = max(int((x2 - x1) / spacing) + 1, self.minNbar)

        xVals = np.linspace(x1, x2, Nlines)

        q1, q2 = self.loadBox.fout
        yVals = np.linspace(q1, q2, Nlines)

        # The top/bottom lines .
        ydatum = self.loadBox.datum
        xbar = [x1, x2]
        yBardatum = [ydatum, ydatum]
        yBarLinear = [q1, q2]

        plt.plot(xbar, yBardatum, linewidth=barWidth, c=barC)
        plt.plot(xbar, yBarLinear, linewidth=barWidth, c=barC)

        for ii in range(Nlines):
            xline = xVals[ii]
            yLine = yVals[ii]

            # plot just the line with no arrow
            if abs(yLine - ydatum) > minLengthCutoff:
                xy0 = (xline, yLine)
                dxy0 = (0, ydatum - yLine)
                load = DiagramElePointLoad(xy0, dxy0, self.plOptions)
                load.plot(ax)

            # plot line and arrow.
            else:
                width = self.plOptions.lw
                ax.plot([xline, xline], [yLine, ydatum], c=barC,
                        linewidth=barWidth * 0.5)


class DiagramEleMoment(AbstractDiagramElement):

    def __init__(self, xy0, diagramOptions: MomentPointLoadOptions,
                 isPositive=False):
        self.xy0 = xy0
        self.options = diagramOptions
        self.c = diagramOptions.c
        self.r = diagramOptions.r

        self.rotationAngle = diagramOptions.rotationAngle

        self.isPositive = isPositive

    def _getFixedSupportCords(self, positive):


        r = self.r
        arrow = r / 4
        arclength = 1 * 2 * np.pi

        # Get base rectangle point.
        t = np.linspace(0.0, 0.8, 31) * arclength
        x = r * np.cos(t)
        y = r * np.sin(t)

        if positive:
            ind = -1
            x0c = x[ind]
            y0c = y[ind]
            xarrow = [x0c - arrow * 1.2, x0c, x0c - arrow * 1.2]
            yarrow = [y0c + arrow * 1.5, y0c, y0c - arrow * 1.5]

        if not positive:
            ind = 0
            x0c = x[ind]
            y0c = y[ind]
            xarrow = [x0c - arrow * 1.5, x0c, x0c + arrow * 1.5]
            yarrow = [y0c + arrow * 1.2, y0c, y0c + arrow * 1.2]

        return x, y, xarrow, yarrow

    def plot(self, ax):

        lw = self.options.lw
        x, y, xarrow, yarrow = self._getFixedSupportCords(self.isPositive)
        rInner = self.r / 5

        # Define a rotation matrix
        theta = np.radians(self.rotationAngle)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))

        # rotate the vectors
        xy = np.column_stack([x, y])
        xyArrow = np.column_stack([xarrow, yarrow])
        xyOut = np.dot(xy, R.T)
        xyArrowOut = np.dot(xyArrow, R.T)

        # Shift to the correct location

        x0 = self.xy0[0]
        xyOut[:, 0] += x0
        xyArrowOut[:, 0] += x0
        xy0 = [x0, 0]

        c = self.options.c
        ax.add_patch(Circle(xy0, rInner, facecolor=c, fill=True, zorder=2, lw=lw))

        plt.plot(xyOut[:, 0], xyOut[:, 1])
        plt.plot(xyArrowOut[:, 0], xyArrowOut[:, 1], c=c)


class EleLoadBox:
    def __init__(self, x: tuple[float], y: tuple[float], fint: tuple[float] = None,
                 intDatum: float = None):
        self.x = x
        self.y = y

        self.x.sort()
        self.y.sort()

        if fint == None:
            fint = [1, 1]

        self.fint = fint
        self.fout = [self._interpolate(fint[0]), self._interpolate(fint[1])]

        # If the internal datum is manually set
        if intDatum:
            self.intDatum = intDatum
            self.datum = self._interpolate(intDatum)

            sign1 = np.sign(self.fout[0])
            sign2 = np.sign(self.fout[1])
            if sign1 == sign2 >= 0:
                self.changedDirection = False
            else:
                self.changedDirection = True

        # If there is no internal datum, this is the typical case.
        else:
            self._initInternalDatum()

    def setDatum(self, datum):
        dy = datum - self.datum
        self.y = [self.y[0] + dy, self.y[1] + dy]
        self.datum = datum

        fint = self.fint
        self.fout = [self._interpolate(fint[0]), self._interpolate(fint[1])]

    def shiftDatum(self, dy):
        self.y = [self.y[0] + dy, self.y[1] + dy]
        self.datum = self.datum + dy

        fint = self.fint
        self.fout = [self._interpolate(fint[0]), self._interpolate(fint[1])]

    def getInternalDatum(self):
        return self.datum

    def _interpolate(self, fint):
        return (self.y[1] - self.y[0]) * fint + self.y[0]

    def _initInternalDatum(self):

        sign1 = np.sign(self.fout[0])
        sign2 = np.sign(self.fout[1])

        self.datum = 0
        if sign1 >= 0 and sign2 >= 0:
            self.changedDirection = False
            self.intDatum = 0

        elif sign1 <= 0 and sign2 <= 0:
            self.changedDirection = False
            self.intDatum = 1
        else:
            self.changedDirection = True
            dy = self.y[0] - self.y[1]
            self.intDatum = self.y[0] / dy

    @property
    def isConstant(self):
        return self.fint[0] == self.fint[1]
