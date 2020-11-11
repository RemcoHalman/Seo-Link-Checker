// https://docs.cypress.io/api/introduction/api.html

describe("Check the global settings", () => {
  it("Visits the app root url", () => {
    cy.visit("/");
    cy.title().should("include", "Link Status Checker");
    cy.get("header").contains("h1", "TITEL EN SEARCH ICON");
    cy.get("footer").contains("h1", " Created by: Remco Halman ");
  });
});
