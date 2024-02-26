package com.codechallenge.pageobjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class CheckoutStepTwoPage {
    private WebDriver driver;

    public CheckoutStepTwoPage(WebDriver driver) {
        this.driver = driver;
    }

    public void finishCheckout() {
        driver.findElement(By.id("finish")).click();
    }
}
