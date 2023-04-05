# bdweb

[![License](https://img.shields.io/github/license/saltstack/salt)](https://github.com/shuhuang/bdweb/blob/master/LICENSE)

This is the source code for the [BatteryData](https://www.materialsforbatteries.org/) web app based on Django.

To test this web app locally, install the requirements.txt file and make migrations using the following command:

```
python manage.py makemigrations
python manage.py migrate
```

Then run the server:
```
python manage.py runserver
```

## Acknowledgements
This project was financially supported by the [Science and Technology Facilities Council (STFC)](https://www.ukri.org/councils/stfc/), the [Royal Academy of Engineering](https://raeng.org.uk/) (RCSRF1819\7\10) and [Christ's College, Cambridge](https://www.christs.cam.ac.uk/). The Argonne Leadership Computing Facility, which is a [DOE Office of Science Facility](https://science.osti.gov/), is also acknowledged for use of its research resources, under contract No. DEAC02-06CH11357.

## Citation
#### BatteryDataExtractor: battery-aware text-mining software embedded with BERT models
```
@article{huang2022batterydataextractor,
  title={BatteryDataExtractor: battery-aware text-mining software embedded with BERT models},
  author={Huang, Shu and Cole, Jacqueline M},
  journal={Chemical Science},
  volume={13},
  number={39},
  pages={11487--11495},
  year={2022},
  publisher={Royal Society of Chemistry}
}
```
[![DOI](https://zenodo.org/badge/DOI/10.1039/D2SC04322J.svg)](https://doi.org/10.1039/D2SC04322J)


#### BatteryBERT: A Pre-trained Language Model for Battery Database Enhancement
```
@article{huang2022batterybert,
  title={BatteryBERT: A Pretrained Language Model for Battery Database Enhancement},
  author={Huang, Shu and Cole, Jacqueline M},
  journal={J. Chem. Inf. Model.},
  year={2022},
  doi={10.1021/acs.jcim.2c00035},
  url={DOI:10.1021/acs.jcim.2c00035},
  pages={DOI: 10.1021/acs.jcim.2c00035},
  publisher={ACS Publications}
}
```
[![DOI](https://zenodo.org/badge/DOI/10.1021/acs.jcim.2c00035.svg)](https://doi.org/10.1021/acs.jcim.2c00035)

#### A database of battery materials auto-generated using ChemDataExtractor
```
@article{huang2020database,
  title={A database of battery materials auto-generated using ChemDataExtractor},
  author={Huang, Shu and Cole, Jacqueline M},
  journal={Scientific Data},
  volume={7},
  number={1},
  pages={1--13},
  year={2020},
  publisher={Nature Publishing Group}
}
```
[![DOI](https://zenodo.org/badge/DOI/10.1038/s41597-020-00602-2.svg)](https://doi.org/10.1038/s41597-020-00602-2)
