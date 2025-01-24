'''
This code is for testing functioning of different modalities 
'''


import os
import pathlib

import SimpleITK as sitk
import pytest
import pydicom

from imgtools.io import read_dicom_auto
from imgtools.ops import StructureSetToSegmentation

@pytest.fixture
def modalities_path():
    curr_path = pathlib.Path(__file__).parent.parent.resolve()
    print(os.listdir(curr_path))
    
    # qc_path = pathlib.Path(os.path.join(curr_path, "data", "Head-Neck-PET-CT", "HN-CHUS-082"))
    # path = {}
    # path["CT"] = os.path.join(qc_path, "08-27-1885-CA ORL FDG TEP-06980/3.000000-Merged-05195")
    # path["RTSTRUCT"] = os.path.join(qc_path, "08-27-1885-06980/Pinnacle POI-67882")
    # path["RTDOSE"] = os.path.join(qc_path, "08-27-1885-06980/89632")
    # path["PT"] = os.path.join(qc_path, "08-27-1885-TEP cancerologique TEP-06980/552650.000000-LOR-RAMLA-72508")
    qc_path = pathlib.Path(curr_path, "data", "Head-Neck-PET-CT", "HN-CHUS-052").as_posix()
    assert os.path.exists(qc_path), "Dataset not found"
    
    path = {}
    path["CT"] = pathlib.Path(qc_path, "08-27-1885-CA ORL FDG TEP POS TX-94629/3.000000-Merged-06362").as_posix()
    path["RTSTRUCT"] = pathlib.Path(qc_path, "08-27-1885-OrophCB.0OrophCBTRTID derived StudyInstanceUID.-94629/Pinnacle POI-41418").as_posix()
    path["RTDOSE"] = pathlib.Path(qc_path, "08-27-1885-OrophCB.0OrophCBTRTID derived StudyInstanceUID.-94629/11376").as_posix()
    path["PT"] = pathlib.Path(qc_path, "08-27-1885-CA ORL FDG TEP POS TX-94629/532790.000000-LOR-RAMLA-44600").as_posix()
    return path

@pytest.mark.parametrize("modalities", ["CT", "RTSTRUCT", "RTDOSE", "PT"])
def test_modalities(modalities, modalities_path):
    path = modalities_path
    img = read_dicom_auto(path["CT"]).image
    if modalities != "RTSTRUCT":
        #Checks for dimensions
        dcm = pydicom.dcmread(pathlib.Path(path[modalities],os.listdir(path[modalities])[0]).as_posix()).pixel_array
        instances = len(os.listdir(path[modalities]))
        dicom = read_dicom_auto(path[modalities])
        if modalities == 'CT':
            dicom = dicom.image
        if instances>1: #For comparing CT and PT modalities
            assert dcm.shape == (dicom.GetHeight(),dicom.GetWidth())
            assert instances == dicom.GetDepth()
        else: #For comparing RTDOSE modalties
            assert dcm.shape == (dicom.GetDepth(),dicom.GetHeight(),dicom.GetWidth())
        if modalities == "PT":
            dicom = dicom.resample_pet(img)
            assert dicom.GetSize()==img.GetSize()
        if modalities == "RTDOSE":
            dicom = dicom.resample_dose(img)
            assert dicom.GetSize()==img.GetSize()
    else:
        struc = read_dicom_auto(path[modalities])
        make_binary_mask = StructureSetToSegmentation(roi_names=['GTV.?', 'LARYNX'], continuous=False)
        mask = make_binary_mask(struc, img, {"background": 0}, False)
        A = sitk.GetArrayFromImage(mask)
        assert len(A.shape) == 4
        assert A.shape[0:3] == (img.GetDepth(),img.GetHeight(),img.GetWidth())
