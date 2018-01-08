#!/usr/bin/env python
# coding: utf-8
import click
import json
from idmatch.idcardocr import CardReader


@click.command()
@click.option('--image', default='demo.jpg', help='ID card image path')
@click.option('--template', default='kg', help='ID card template (kg only is available)')
def cardocr(image, template):
    reader = CardReader(template, image)
    print(reader.route())


if __name__ == '__main__':
    cardocr()
