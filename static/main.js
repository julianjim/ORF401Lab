// If the user has never visited ANY aspect of our site (webpages and/or splashpage) then redirect them to splash page.
// If they visited another aspect of our site, but is their first time to a specific webpage, then does not direct them because 
// they have already been on the site and are familiar with our splash page but they can still choose to access the splash page.
function checkCookie() {
    // Checks if we've visited any aspect of our site for the first time
    if (!getCookie('first_visit')) {
        setCookie('first_visit', 1, 90); // Set the cookie for 90 days 
        window.location.href = 'https://fathomless-temple-75549-a913d17d22f1.herokuapp.com'; // Redirect to the splash page
    }
}


function getCookie(c_name) {

    var i,x,y,ARRcookies=document.cookie.split(";");
    for (i=0;i<ARRcookies.length;i++){
        x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
        y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
        x=x.replace(/^\s+|\s+$/g,"");
        if (x==c_name) {
            return unescape(y);
        }
    }
}

function setCookie(c_name,value,exdays) {

    var exdate=new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value=escape(value) + ((exdays==null) ? "" : ";expires="+exdate.toUTCString());
    document.cookie=c_name + "=" + c_value;
}

function checkForm(form) {
    
    // Check if the search field is empty
    if (form.elements[0].value == '' && form.elements[1].value == '') {
        alert('Please enter a search term before submitting.');
        return false;
    }
    
    // Check if the search term is 'Elon Musk'
    if (form.elements[0].value.localeCompare('elon musk', undefined, { sensitivity: 'accent' }) === 0) {
        alert('He’s not here');
        return false;
    }

    return true;
}