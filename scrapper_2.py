from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import csv

#NASA Exoplanet URL

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

time.sleep(10)
planets_data = []
headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date","hyperlink","planet_type","planet_radius","orbital_radius","orbital_period","eccentricety"]