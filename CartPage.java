package com.codechallenge.pageobjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class CartPage {
    private WebDriver driver;

    public CartPage(WebDriver driver) {
        this.driver = driver;
    }

    public void checkout() {
        driver.findElement(By.id("checkout")).click();
    }
}
