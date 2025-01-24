from typing import Any
from xml.dom import Node, minidom

from nerdd_module import Converter, ConverterConfig
from rdkit.Chem import Mol
from rdkit.Chem.Draw import MolDraw2DSVG

__all__ = ["MolToImageConverter"]

default_width = 300
default_height = 180


class MolToImageConverter(Converter):
    def _convert(self, input: Any, context: dict) -> Any:
        width = self.result_property.image_width
        height = self.result_property.image_height

        if width is None:
            width = default_width
        if height is None:
            height = default_height

        mol = input
        if mol is None:
            return None

        assert isinstance(mol, Mol), f"Expected RDKit Mol object, but got {type(mol)}"

        svg = MolDraw2DSVG(width, height)

        # remove background
        opts = svg.drawOptions()
        opts.clearBackground = False

        # add highlight circles around atoms during drawing
        # (we will remove them later in post processing)
        atoms = range(mol.GetNumAtoms())
        colors = [[(0.8, 1, 1)]] * mol.GetNumAtoms()
        radii = [0.5] * mol.GetNumAtoms()
        atom_highlight = dict(zip(atoms, colors))
        atom_radii = dict(zip(atoms, radii))
        svg.DrawMoleculeWithHighlights(mol, "", atom_highlight, {}, atom_radii, [])
        svg.FinishDrawing()

        # post process SVG
        xml = svg.GetDrawingText()
        tree = minidom.parseString(xml)
        root = tree.getElementsByTagName("svg")[0]

        # manipulate highlight circles
        for ellipse in root.getElementsByTagName("ellipse"):
            # make highlight circles invisible
            ellipse.setAttribute("style", "fill: transparent")

            # remove highlight circle from parent
            parent = ellipse.parentNode
            parent.removeChild(ellipse)

            # add highlight circle at the end of parent
            parent.appendChild(ellipse)

        # compress svg by removing whitespace nodes
        # Note: removing nodes immediately would mess up the iteration
        #   --> collect nodes to remove first and remove them in a second step
        remove_nodes = []
        for child in root.childNodes:
            if child.nodeType == Node.TEXT_NODE and child.data.strip() == "":
                remove_nodes.append(child)
        for node in remove_nodes:
            root.removeChild(node)

        xml = tree.toxml()

        return xml

    config = ConverterConfig(data_types="mol", output_formats="json")
