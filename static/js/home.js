 
    function predictnews() {
        let loader = document.getElementById('loader-id');
        let articleTitle = document.getElementById("article-title");
        let articleAuthor = document.getElementById("article-author");
        let articleText = document.getElementById("article-text");
        let resultBanner = document.getElementById("result-banner");
        let news=articleTitle.value + ' ' + articleAuthor.value + ' ' + articleText.value; 

        console.log(loader);
        loader.style.display = 'inline';
        console.log(loader.style);
        resultBanner.textContent = '';
        console.log(articleText.value)
        if(articleText.value=='' && articleText.value=='' && articleText.value==''){
            loader.style.display = 'none';
            resultBanner.textContent ="plese fill data in atleast one box";
            articleText.style.border = "3px solid red";
            articleTitle.style.border = "3px solid red";
            articleAuthor.style.border = "3px solid red";
        }
        else{
            let prediction = getPrediction(news);
            
            prediction.then(function (response) {
                loader.style.display = 'none';
                if (response === "real") {
                    articleTitle.style.border = "3px solid green";
                    articleAuthor.style.border = "3px solid green";
                    articleText.style.border = "3px solid green";
                    resultBanner.style.color = "green";
                    resultBanner.textContent = "Real news!";
                } else {
                    articleTitle.style.border = "3px solid red";
                    articleAuthor.style.border = "3px solid red";
                    articleText.style.border = "3px solid red";
                    resultBanner.style.color = "red";
                    resultBanner.textContent = "Fake news!";
                }}, function (error) {
                    console.error("Prediction API call failed with error: " + error);
                });
        } 
}


function getdata() {
        
        let articleTitle = document.getElementById("article-title");
        let articleAuthor = document.getElementById("article-author");
        let articleText = document.getElementById("article-text");
        let resultBanner = document.getElementById("result-banner");
        resultBanner.textContent=' ';
        
       
        //let news = getnews();
        let url = '/random';
        fetch(url, {method: "GET"})
        .then(res => res.json())
        .then(function (res) {
            articleTitle.textContent=res.title;
            articleAuthor.textContent=res.author;
            articleText.textContent=res.text;

        },function (error) {
                console.error("random API call failed with error: " + error);
            });
        
}
