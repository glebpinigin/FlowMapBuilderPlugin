# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FlowMapBuilder
                                 A QGIS plugin
 This plugin builds flow maps
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-03-23
        copyright            : (C) 2022 by Gleb Pinigin
        email                : pinigin1514@live.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

import sys, os
sys.path.insert(0, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), ''))+'\\flowmapper')

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load FlowMapBuilder class from file FlowMapBuilder.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .flow_map_builder import FlowMapBuilder
    return FlowMapBuilder(iface)
