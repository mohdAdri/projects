package com.codechallenge.pageobjects;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class ProductsPage {
    private WebDriver driver;

    public ProductsPage(WebDriver driver) {
        this.driver = driver;
    }

    public void addToCart(String productName) {
    	//WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5));
    	//WebElement element = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//div[text()='Sauce Labs Backpack']/following-sibling::button")));

        //WebElement addToCartButton = driver.findElement(By.xpath("//div[text()='" + productName + "']/following-sibling::button"));
    	WebElement addToCartButton = driver.findElement(By.id("item_4_title_link"));
        
    	addToCartButton.click();
    }

    public void openCart() {
        driver.findElement(By.id("shopping_cart_container")).click();
    }
}
