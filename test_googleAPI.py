import pytest
import os
from googleAPI import imageScraper

def test_num_images():
    items_list = [
        'Pillar',
        'Television',
        'Photo Frame',
        'Lamp',
        'Fireplace',
        'Flooring',
        'Sofa',
        'Table', 
        'Service Men',
        'Window'
    ]

    for item in items_list:
        targetImage = imageScraper(item)
        file_list = os.listdir('./'+item)
        assert len(file_list) == 100 

