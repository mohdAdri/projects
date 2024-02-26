package com.codechallenge.pageobjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class CheckoutStepOnePage {
    private WebDriver driver;

    public CheckoutStepOnePage(WebDriver driver) {
        this.driver = driver;
    }

    public void enterCheckoutInformation(String firstName, String lastName, String zipCode) {
        driver.findElement(By.id("first-name")).sendKeys(firstName);
        driver.findElement(By.id("last-name")).sendKeys(lastName);
        driver.findElement(By.id("postal-code")).sendKeys(zipCode);
        driver.findElement(By.id("continue")).click();
    }
}
