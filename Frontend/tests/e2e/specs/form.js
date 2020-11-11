describe("Check content screen", () => {
  it("Visits the app root url", () => {
    cy.visit("/");
    cy.get("#input-form") // Main content
      .contains("button", "Search page");
  });
});
