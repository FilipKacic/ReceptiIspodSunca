document.addEventListener('DOMContentLoaded', function() {
    // alert('Heaveno world!');
});

function saveRecipeAsText() {
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