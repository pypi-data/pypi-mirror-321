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
from abc import ABC, abstractmethod
from loads import PointLoadOptions, DistLoadOptions, LinLoadOptions, MomentPointLoadOptions
from configure import supportDiagramOptions, LabelOptions
from baseclasses import BeamOptions


class AbstractDiagramElement(ABC):
    @abstractmethod
    def plot(self):
        pass


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