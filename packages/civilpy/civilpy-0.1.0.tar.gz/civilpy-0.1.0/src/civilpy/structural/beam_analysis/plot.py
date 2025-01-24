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
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from abc import ABC, abstractmethod
from matplotlib.patches import Rectangle, Polygon, Circle

from diagram import (
    supportDiagramOptions,
    PointLoadOptions,
    MomentPointLoadOptions,
    DistLoadOptions,
)
from baseclasses import EleLoadDist, EleLoadLinear
from plot_functions import EleLoadBox, _setForceVectorLengthEle, Boxstacker
from configure import diagramUnits, LabelOptions

@dataclass
class BeamOptions:
    lw:float
    c:float


@dataclass
class LinLoadOptions:
    # GlobalParameters
    baseWidth: float
    c: float  # colour
    arrowWidth: float

    spacing: float
    barWidth: float
    minLengthCutoff: float


class AbstractDiagramElement(ABC):
    @abstractmethod
    def plot(self):

        pass


class DiagramEleFreeSupport:

    def __init__(self, xy, diagramOptions: supportDiagramOptions):
        pass

    def plot(self, ax):

        pass


class DiagramElePinSupport(AbstractDiagramElement):

    def __init__(self, xy0, diagramOptions: supportDiagramOptions):
        self.xy0 = xy0
        self.options = diagramOptions

    def _getPinSupportCords(self, xy0, scale):

        wTriSup = self.options.wTriSup
        hTriSup = self.options.hTriSup
        wRect = self.options.wRect
        hFixedRect = self.options.hFixedRect

        xyTri1 = [xy0[0] - wTriSup / 2, xy0[1] - hTriSup]
        xyTri2 = [xy0[0] + wTriSup / 2, xy0[1] - hTriSup]
        xyTri = [xyTri1, xyTri2, xy0]

        xy0Rect = [xy0[0] - wRect / 2, xy0[1] - hTriSup - hFixedRect]

        xyLine = [[xy0[0] - wRect / 2, xy0[0] + wRect / 2],
                  [xy0[1] - hTriSup - hFixedRect, xy0[1] - hTriSup - hFixedRect]]

        return xyTri, xy0Rect, xyLine

    def _plotPinGeom(self, ax, xy0, xyTri, xy0Rect, xyLine):

        #
        lw = self.options.lw
        hatch = self.options.hatch
        wRect = self.options.wRect
        r = self.options.r
        hFixedRect = self.options.hFixedRect

        ax.add_patch(Polygon(xyTri, fill=False, lw=lw))
        ax.add_patch(Rectangle(xy0Rect, wRect, hFixedRect, ec='black', fc='white', hatch=hatch, lw=lw))
        ax.plot(xyLine[0], xyLine[1], c='white', lw=lw)
        ax.add_patch(Circle(xy0, r, facecolor='white', ec='black', fill=True, zorder=1, lw=lw))

    def plot(self, ax):

        scale = self.options.scale
        xyTri, xy0Rect, xyLine = self._getPinSupportCords(self.xy0, scale)
        self._plotPinGeom(ax, self.xy0, xyTri, xy0Rect, xyLine)


class DiagramEleRollerSupport(DiagramElePinSupport):

    def __init__(self, xy0, diagramOptions: supportDiagramOptions):
        self.xy0 = xy0
        self.options = diagramOptions

    def _getRollerSupportCords(self, xy0, scale):


        lineOffset = self.options.lineOffset_roller
        hTriSup = self.options.hTriSup
        hRollerGap = self.options.hRollerGap
        wRect = self.options.wRect

        # The gap starts a the botom-left surface of the roller
        xy0gap = [xy0[0] - wRect / 2, xy0[1] - hTriSup + lineOffset]

        # The line starts at the top of the gap
        xyRollerLine = [[xy0[0] - wRect / 2, xy0[0] + wRect / 2],
                        [xy0[1] - hTriSup + hRollerGap + lineOffset,
                         xy0[1] - hTriSup + hRollerGap + lineOffset]]

        return xy0gap, xyRollerLine

    def _plotRollerGeom(self, ax, xy0gap, xyRollerLine):
        lw = self.options.lw
        hRollerGap = self.options.hRollerGap
        wRect = self.options.wRect

        ax.add_patch(Rectangle(xy0gap, wRect, hRollerGap, color='white', lw=lw))
        ax.plot(xyRollerLine[0], xyRollerLine[1], color='black', lw=lw)

    def plotRoller(self, ax):

        xy0 = self.xy0
        scale = self.options.scale
        xyTri, xy0Rect, xyLine = self._getPinSupportCords(xy0, scale)
        self._plotPinGeom(ax, xy0, xyTri, xy0Rect, xyLine)
        xy0gap, xyRollerLine = self._getRollerSupportCords(xy0, scale)
        self._plotRollerGeom(ax, xy0gap, xyRollerLine)

    def plot(self, ax):


        self.plotRoller(ax)


class DiagramEleFixedSupport(AbstractDiagramElement):

    def __init__(self, xy0, diagramOptions: supportDiagramOptions,
                 isLeft=True):
        self.xy0 = xy0
        self.options = diagramOptions
        self.isLeft = isLeft

    def _getFixedSupportCords(self, xy0, isLeft):


        wRect = self.options.wRect
        hFixedRect = self.options.hFixedRect

        if isLeft:
            xy0Rect = [xy0[0] - hFixedRect, xy0[1] - wRect / 2]

            xyLine = [[xy0[0], xy0[0] - hFixedRect, xy0[0] - hFixedRect, xy0[0]],
                      [xy0[1] + wRect / 2, xy0[1] + wRect / 2,
                       xy0[1] - wRect / 2, xy0[1] - wRect / 2]]
        else:
            xy0Rect = [xy0[0], xy0[1] - wRect / 2]
            xyLine = [[xy0[0], xy0[0] + hFixedRect, xy0[0] + hFixedRect, xy0[0]],
                      [xy0[1] + wRect / 2, xy0[1] + wRect / 2,
                       xy0[1] - wRect / 2, xy0[1] - wRect / 2]]

        return xy0Rect, xyLine

    def plot(self, ax):


        lw = self.options.lw
        hFixedRect = self.options.hFixedRect
        hatch = self.options.hatch
        wRect = self.options.wRect
        xy0 = self.xy0

        isLeft = self.isLeft
        xy0Rect, xyLine = self._getFixedSupportCords(xy0, isLeft)
        ax.add_patch(Rectangle(xy0Rect, hFixedRect, wRect, ec='black',
                               fc='white', hatch=hatch, lw=lw))
        ax.plot(xyLine[0], xyLine[1], c='white', lw=lw)


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


class DiagramEleLabel:

    def __init__(self, xy0, label, labelOptions):
        self.xy0 = xy0
        self.label = label
        self.labelOffset = labelOptions.labelOffset
        self.textKwargs = labelOptions.textKwargs

    def plot(self, ax):
        x = self.xy0[0] + self.labelOffset
        y = self.xy0[1] + self.labelOffset
        ax.text(x, y, self.label, self.textKwargs)



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


class DiagramEleBeam:
    def __init__(self, xy0, xy1, diagramOptions: BeamOptions):
        self.xy0 = xy0
        self.xy1 = xy1
        self.options = diagramOptions

    def plot(self, ax):
        xy0 = self.xy0
        xy1 = self.xy1
        lw = self.options.lw
        c = self.options.c
        ax.plot([xy0[0], xy1[0]], [xy0[1], xy1[1]], lw=lw, c=c)

class BasicDiagramPlotter:
    supportTypeDict = {'free': DiagramEleFreeSupport,
                       'pinned': DiagramElePinSupport,
                       'roller': DiagramEleRollerSupport,
                       'fixed': DiagramEleFixedSupport}

    def __init__(self, scale=1, supScale=0.8, L=1):
        diagramOptions = BasicOptionsDiagram(scale, supScale)
        self.supportParams = diagramOptions.getSupportDiagramOptions()
        self.labelParams = diagramOptions.getLabelOptions()
        self.plOptions = diagramOptions.getPointLoadOptions()
        self.momentParams = diagramOptions.getMomentPointLoadOptions()
        self.distParams = diagramOptions.getDistLoadOptions()
        self.linParams = diagramOptions.getLinLoadOptions()

        self.pldistOptions = diagramOptions.getPointLoadDistOptions()

        self.beamParams = diagramOptions.getBeamOptions()

    def setEleLoadLineSpacing(self, baseSpacing):
        self.distParams.spacing = self.distParams.spacing * baseSpacing
        self.linParams.spacing = self.linParams.spacing * baseSpacing

    def _checkSupType(self, supType):
        if supType not in self.supportTypeDict:
            options = list(self.supportTypeDict)
            raise Exception(f'Recived {supType}, expected one of {options}')

    def plotBeam(self, ax, xy0, xy1):
        beam = DiagramEleBeam(xy0, xy1, self.beamParams)
        beam.plot(ax)

    def plotSupport(self, ax, xy, supType, kwargs):
        self._checkSupType(supType)
        supportClass = self.supportTypeDict[supType]
        support = supportClass(xy, self.supportParams, **kwargs)
        support.plot(ax)

    def plotLabel(self, ax, xy, label):
        pl = DiagramEleLabel(xy, label, self.labelParams)
        pl.plot(ax)

    def plotPointForce(self, ax, xy, Pxy):
        pl = DiagramElePointLoad(xy, Pxy, self.plOptions)
        pl.plot(ax)

    def plotPointMoment(self, ax, xy, isPositive):
        pl = DiagramEleMoment(xy, self.momentParams, isPositive=isPositive)
        pl.plot(ax)

    def plotElementDistributedForce(self, ax, loadBox):
        pl = DiagramEleLoadDistributed(loadBox, self.distParams, self.pldistOptions)
        pl.plot(ax)

    def plotElementLinearForce(self, ax, loadBox):
        pl = DiagramEleLoadLinear(loadBox, self.linParams, self.pldistOptions)
        pl.plot(ax)

    def _initPlot(self, figSize, xlims, ylims, dpi=300):
        dy = ylims[-1] - ylims[0]
        fig, ax = plt.subplots(constrained_layout=True, figsize=(figSize, dy), dpi=300)
        ax.axis('equal')
        ax.axis('off')
        ax.set_xlim(xlims)
        ax.set_ylim(ylims)
        return fig, ax


class BeamPlotter2D:
    def __init__(self, beam, figsize=8, units='environment'):


        self.beam = beam
        self.figsize = figsize

        if units == 'environment':
            self.unitHandler = diagramUnits.activeEnv
        else:
            self.unitHandler = diagramUnits.getEnvironment(units)

        L = beam.getLength()
        xscale = L / self.figsize
        self.xscale = xscale
        baseSpacing = self.beam.getLength() / self.xscale

        self.plotter: BasicDiagramPlotter = BasicDiagramPlotter(L=L)
        self.plotter.setEleLoadLineSpacing(baseSpacing)

        xlims = beam.getxLims()
        self.xmin = xlims[0]
        self.xmax = xlims[0]

        self.xlimsPlot = [(xlims[0] - L / 20) / xscale, (xlims[1] + L / 20) / xscale]

        self.ylimsPlot = [-L / 10 / xscale, L / 10 / xscale]

        self.plottedNodeIDs = []

    def plot(self, plotLabel=False, labelForce=True,
             plotForceValue=True, **kwargs):

        args = (self.figsize, self.xlimsPlot, self.ylimsPlot)
        self.fig, self.ax = self.plotter._initPlot(*args)
        self.plotSupports()

        pfplot, efplot = None, None
        if self.beam.pointLoads:
            pfplot = self.plotPointForces()
        if self.beam.pointLoads and plotLabel:
            self.plotPointForceLables(pfplot, labelForce, plotForceValue)
        if self.beam.eleLoads:
            efplot, xcoords = self.plotEleForces()
        if self.beam.eleLoads and plotLabel:
            self.plotDistForceLables(efplot, xcoords, labelForce, plotForceValue)

        if plotLabel:
            self.plotLabels()

        self.plotBeam()

        if (not (pfplot is None)) or (not (efplot is None)):
            self._adjustPlot(pfplot, efplot)

    def _adjustPlot(self, pfplot, efplot):
        if (pfplot is None):
            pfplot = (0)
        if (efplot is None):
            efplot = (0)

        fmax = max(np.max(pfplot), np.max(efplot))
        fmin = min(np.min(pfplot), np.min(efplot))
        if fmin < self.ylimsPlot[0]:
            self.ylimsPlot[0] = fmin
        if self.ylimsPlot[1] < fmax:
            self.ylimsPlot[1] = fmax

        self.ax.set_ylim(self.ylimsPlot)

    def plotBeam(self):

        xlims = self.beam.getxLims()
        xy0 = [xlims[0] / self.xscale, 0]
        xy1 = [xlims[1] / self.xscale, 0]
        self.plotter.plotBeam(self.ax, xy0, xy1)

    def plotSupports(self):


        for node in self.beam.nodes:
            fixityType = node.getFixityType()
            x = node.getPosition()
            xy = [x / self.xscale, 0]


            kwargs = {}
            if fixityType == 'fixed' and x == self.xmin:
                kwargs = {'isLeft': True}

            if fixityType == 'fixed' and not x == self.xmin:
                kwargs = {'isLeft': False}

            self.plotter.plotSupport(self.ax, xy, fixityType, kwargs)

    def _addLabelToPlotted(self, nodeID):
        self.plottedNodeIDs.append(nodeID)

    def _checkIfLabelPlotted(self, nodeID):
        check = nodeID in self.plottedNodeIDs
        return check

    def plotLabels(self):


        for node in self.beam.nodes:
            label = node.label
            x = node.getPosition()

            if label and (self._checkIfLabelPlotted(node.ID) != True):
                xy = [x / self.xscale, 0]
                self.plotter.plotLabel(self.ax, xy, label)
                self._addLabelToPlotted(node.ID)

    def _getValueText(self, diagramType, forceValue):

        unit = self.unitHandler[diagramType].unit
        scale = self.unitHandler[diagramType].scale
        Ndecimal = self.unitHandler[diagramType].Ndecimal

        # Round force
        forceValue *= scale
        if Ndecimal == 0:
            forceValue = round(forceValue)
        else:
            forceValue = round(forceValue * 10 ** Ndecimal) / 10 ** Ndecimal
        return forceValue, unit

    def plotPointForceLables(self, fplot, labelForce, plotForceValue):


        inds = range(len(self.beam.pointLoads))
        for ii, force in zip(inds, self.beam.pointLoads):
            Px, Py, Mx = fplot[ii]
            isMoment = False
            if Mx != 0:
                isMoment = True
                Py = -0.15
                diagramType = 'moment'
                fText = force.P[2]
            else:
                # shift the force down so it fits in the diagram!
                Py += 0.15
                diagramType = 'force'
                fText = np.sum(force.P[:2] ** 2) ** 0.5

            # get the label from the node - it's store there and not on the force.
            labelBase = force.label
            # labelBase = self.beam.nodes[force.nodeID - 1].label
            label = ''

            if labelBase and labelForce and isMoment:
                label += f'$M_{{{labelBase}}}$'  # Tripple brackets needed to make the whole thing subscript

            elif labelBase and labelForce and (not isMoment):
                label += f'$P_{{{labelBase}}}$'
            else:
                pass

            if labelBase and plotForceValue and labelForce:
                valueText, unit = self._getValueText(diagramType, fText)
                label += ' = ' + str(valueText) + "" + unit

            x = force.getPosition()
            xy = [x / self.xscale, -Py]

            if label and self._checkIfLabelPlotted(force.nodeID) != True:
                self.plotter.plotLabel(self.ax, xy, label)
                self._addLabelToPlotted(force.nodeID)

    def plotDistForceLables(self, fplot, xcoords, labelForce, plotForceValue):

        diagramType = 'distForce'
        inds = range(len(self.beam.eleLoads))
        for ii, force in zip(inds, self.beam.eleLoads):
            qx, qy = fplot[ii]
            fText = force.P[1]

            labelBase = force.label
            label = ''

            if labelBase and labelForce:
                label += f'$q_{{{labelBase}}}$'

            if labelBase and plotForceValue and labelForce:
                valueText, unit = self._getValueText(diagramType, fText)
                label += ' = ' + str(valueText) + "" + unit

            x1, x2 = xcoords[ii]
            aMid = (x1 + x2) / 2
            xy = [aMid, -qy]  # note, aMid has already been scaled
            self.plotter.plotLabel(self.ax, xy, label)

    def _getForceVectorLengthPoint(self, forces, vectScale=1):

        fscale0 = 0.4
        fstatic0 = 0.3

        # Normalize forces
        forces = np.array(forces)
        signs = np.sign(forces)

        # The maximum force in each direction
        Fmax = np.max(np.abs(forces), 0)

        # Avoid dividing by zero later
        Inds = np.where(np.abs(Fmax) == 0)
        Fmax[Inds[0]] = 1

        # Find all force that are zero. These should remain zero
        Inds0 = np.where(np.abs(forces) == 0)

        # Plot the static portion, and the scale port of the force
        fscale = fscale0 * abs(forces) / Fmax
        fstatic = fstatic0 * np.ones_like(forces)
        fstatic[Inds0[0], Inds0[1]] = 0

        fplot = (fscale + fstatic) * signs

        return fplot * vectScale

    def plotPointForces(self):

        forces = []
        xcoords = []
        for force in self.beam.pointLoads:
            forces.append(force.P)
            xcoords.append(force.x / self.xscale)
        fplot = self._getForceVectorLengthPoint(forces)
        NLoads = len(forces)

        for ii in range(NLoads):
            Px, Py, Mx = fplot[ii]
            x = xcoords[ii]
            if (Px == 0 and Py == 0):  # if it's a moment, plot it as a moment
                if Mx < 0:
                    postive = True
                else:
                    postive = False
                self.plotter.plotPointMoment(self.ax, (x, 0), postive)
            else:
                self.plotter.plotPointForce(self.ax, (x - Px, -Py), (Px, Py))

        return fplot

    def _plotEleForce(self, box: EleLoadBox):

        Py = box.fout

        if (Py[0] == 0) and (Py[1] == 0):
            print("WARNING: Plotted load has no vertical component.")

        if box.isConstant:
            self.plotter.plotElementDistributedForce(self.ax, box)
        else:
            self.plotter.plotElementLinearForce(self.ax, box)

    def normalizeData(self, data):
        return (data - np.min(data)) / (np.max(data) - np.min(data))

    def _getLinFint(self, Ptmp):


        # fintTemp = list(self.normalizeData(Ptmp))
        # If both are on the positive side
        if 0 < np.sign(Ptmp[0]) and 0 < np.sign(Ptmp[1]):

            if Ptmp[0] < Ptmp[1]:
                fintTemp = [Ptmp[0] / Ptmp[1], 1]
            elif Ptmp[0] == Ptmp[1]:  # If equal the load acts like a constant load
                fintTemp = [1, 1]
            else:
                fintTemp = [1, Ptmp[1] / Ptmp[0]]
            Ptmp = [0, max(Ptmp)]

        # If both are on the negative side side
        elif np.sign(Ptmp[0]) < 0 and np.sign(Ptmp[1]) < 0:

            if Ptmp[0] < Ptmp[1]:
                fintTemp = [0, Ptmp[1] / Ptmp[0]]
            elif Ptmp[0] == Ptmp[1]:  # If equal the load acts like a constant load
                fintTemp = [0, 0]
            else:
                fintTemp = [1 - Ptmp[0] / Ptmp[1], 0]
            Ptmp = [min(Ptmp), 0]

        # If the inputs change sign, just use the normalized value.
        else:
            fintTemp = list(self.normalizeData(Ptmp))
        return Ptmp, fintTemp

    def _getEleForceBoxes(self):


        eleBoxes = []

        for load in self.beam.eleLoads:
            xDiagram = [load.x1 / self.xscale, load.x2 / self.xscale]

            if isinstance(load, EleLoadDist):  # Constant Load
                # Adapt the load so it's a 2D vector
                Ptmp = [0, -load.P[1]]  # !!! The sign is flipped to properly stack
                if -load.P[1] < 0:  # !!! The sign is flipped to properly stack
                    fintTemp = [0, 0]  # start at the bottom if negative
                else:
                    fintTemp = [1, 1]  # start at the top if negative
                eleBoxes.append(EleLoadBox(xDiagram, Ptmp, fintTemp))
            # Arbitary Distributed Load between two points
            elif isinstance(load, EleLoadLinear):
                Ptmp = -load.P[1]  # !!! The sign is flipped to properly stack

                Ptmp, fintTemp = self._getLinFint(Ptmp)
                eleBoxes.append(EleLoadBox(xDiagram, Ptmp, fintTemp))

        eleBoxes = _setForceVectorLengthEle(eleBoxes, vectScale=0.4)
        stacker = Boxstacker(eleBoxes)
        eleBoxes = stacker.setStackedDatums()

        return eleBoxes

    def plotEleForces(self):


        eleBoxes = self._getEleForceBoxes()
        for box in eleBoxes:
            self._plotEleForce(box)

        fplot = [box.y for box in eleBoxes]
        xcoords = [box.x for box in eleBoxes]

        return fplot, xcoords


class BasicOptionsDiagram:
    def __init__(self, scale=1, supScale=0.8):


        self.lw = 1 * scale
        self.scale = scale  # Scales all drawing elements
        self.supScale = supScale  # Scales all drawing elements

        # Beam Propreties
        self.lw_beam = 2 * scale
        self.c_beam = 'black'

        # Point Load Propreties
        self.w_PointLoad = 0.03 * scale
        self.c_PointLoad = 'C0'
        self.c_PointLoadDist = 'grey'
        # changes the offset from the point in x/y
        self.labelOffset = 0.1 * scale

        # Pin support geometry variables
        self.r = 0.08 * scale * supScale
        self.hTriSup = 0.3 * scale * supScale
        self.wTriSup = 2 * self.hTriSup

        # Parameters for the rectangle below the pin support
        self.hFixedRect = 0.2 * scale * supScale
        self.marginFixedSup = 0.2 * scale * supScale
        self.hatch = '/' * int((3 / (scale * supScale)))
        self.wRect = self.wTriSup + self.marginFixedSup

        self.lineOffset_roller = self.hFixedRect / 10
        self.hRollerGap = self.hFixedRect / 4
        self.y0 = 0

        # Point Load
        self.lw_pL = 0.03 * scale  # The width of the
        # self.lw_pLbaseWidth = 0.01 * scale # The width of the
        self.arrowWidth = 5 * self.lw_pL

        # Moment Point Load
        self.r_moment = 0.15
        self.rotationAngle = 30
        self.c_moment = 'C0'

        # Distributed Load Propreties
        self.c_dist_bar = 'grey'
        self.spacing_dist = (1 / 20)
        self.barWidth = 1.2 * scale

        self.lw_pL_dist = 0.015
        self.arrowWidth_pL_dist = 5 * self.lw_pL_dist

        # Linear Distributed Load Options
        self.minLengthCutoff = 0.075 * self.scale

        # label Options
        self.labelOffset = 0.1 * scale
        self.textSize = 12 * scale

    def getSupportDiagramOptions(self):
        args = [self.lw, self.scale, self.supScale,
                self.r, self.hTriSup, self.wTriSup, self.hFixedRect,
                self.marginFixedSup, self.hatch, self.wRect,
                self.lineOffset_roller,
                self.hRollerGap, self.y0]

        return supportDiagramOptions(*args)

    def getPointLoadOptions(self):
        args = [self.lw_pL, self.c_PointLoad, self.arrowWidth]
        return PointLoadOptions(*args)

    def getPointLoadDistOptions(self):
        args = [self.lw_pL_dist, self.c_dist_bar, self.arrowWidth_pL_dist]
        return PointLoadOptions(*args)

    def getMomentPointLoadOptions(self):
        args = [self.lw_pL, self.c_moment, self.arrowWidth, self.r_moment,
                self.rotationAngle]

        return MomentPointLoadOptions(*args)

    def getDistLoadOptions(self):
        args = [self.lw, self.c_dist_bar, self.arrowWidth, self.spacing_dist,
                self.barWidth]

        return DistLoadOptions(*args)

    def getLinLoadOptions(self):
        args = [self.lw, self.c_dist_bar, self.arrowWidth, self.spacing_dist,
                self.barWidth, self.minLengthCutoff]

        return LinLoadOptions(*args)

    def getLabelOptions(self):
        args = [self.labelOffset, self.textSize]

        return LabelOptions(*args)

    def getBeamOptions(self):
        args = [self.lw_beam, self.c_beam]
        return BeamOptions(*args)