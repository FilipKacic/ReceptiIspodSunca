document.addEventListener('DOMContentLoaded', function() {
    /* active nav link */
    const allRecipesLink = document.querySelector('nav ul li:nth-child(1) a');
    const userRecipesLink = document.querySelector('nav ul li:nth-child(2) a');

    allRecipesLink.addEventListener('click', function(event) {
        allRecipesLink.classList.add('active');
        userRecipesLink.classList.remove('active');
    });

    userRecipesLink.addEventListener('click', function(event) {
        userRecipesLink.classList.add('active');
        allRecipesLink.classList.remove('active');
    });

    /* confirmation of deletion */
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const url = this.getAttribute('data-url');
            const confirmDelete = confirm('Potvrdite brisanje recepta...');
            if (confirmDelete) {
                window.location.href = url;
            }
        });
    });
});

function downloadRecipeAsText() {
    // gets the content of the recipe div
    const recipeDiv = document.getElementById('recipe');
    const recipeContent = recipeDiv.innerText;
    // gets the recipe name from the data attribute
    const recipeName = recipeDiv.getAttribute('data-recipe-name');
    // creates a blob from the text
    const blob = new Blob([recipeContent], { type: 'text/plain' });
    // creates a link element
    const link = document.createElement('a');
    // sets the download attribute with a filename
    link.download = recipeName + '.txt';
    // creates a URL for the Blob and sets it as the href attribute
    link.href = window.URL.createObjectURL(blob);
    // append the link to the body
    document.body.appendChild(link);
    // programmatically click the link to trigger the download
    link.click();
    // removes the link from the document
    document.body.removeChild(link);
}
