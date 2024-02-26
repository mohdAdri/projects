package com.codechallenge.test.api;

import io.restassured.RestAssured;
import org.junit.jupiter.api.Test;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

public class CommentsApiTest {

    @Test
    public void testGetComments() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";

        given()
            .when()
            .get("/comments/3")
            .then()
            .statusCode(200)
            .body("name", equalTo("odio adipisci rerum aut animi"))
            .body("email", equalTo("Nikita@garfield.biz"));
    }

    @Test
    public void testPostComments() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";

        given()
            .header("Content-type", "application/json")
            .and()
            .body("{\"postId\": 1, \"name\": \"Melissa\", \"email\": \"abc@gmail.com\"}")
            .when()
            .post("/comments")
            .then()
            .statusCode(201)
            .body("id", notNullValue()); // Usually, we verify the 'id' is not null or some expected value
    }

    @Test
    public void testGetUserDetails() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";

        given()
            .when()
            .get("/users/6")
            .then()
            .statusCode(200)
            .body("address.street", equalTo("Norberto Crossing"))
            .body("address.city", equalTo("South Christy"));
    }
}
