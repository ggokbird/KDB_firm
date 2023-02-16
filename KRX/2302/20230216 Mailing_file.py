# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:39:15 2023

@author: 221016
"""

from selenium import webdriver

# Create a new Chrome webdriver
driver = webdriver.Chrome()

# Navigate to the page with the printer settings
driver.get("http://example.com/printer-settings")

# Select the desired printer from the dropdown
printer_dropdown = driver.find_element_by_id("printer-dropdown")
printer_dropdown.select_by_value("desired-printer")

# Click the "Print" button
print_button = driver.find_element_by_id("print-button")
print_button.click()

# Save the PDF file
driver.save_screenshot("file.pdf")

# Close the webdriver
driver.close()