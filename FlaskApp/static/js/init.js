var $_Tawk_API = {},
    $_Tawk_LoadStart = new Date();

(function($) {
    $(function() {
        $('.button-collapse').sideNav();
        $('.parallax').parallax();

        // Start of Tawk.to Script
        var scriptElement = document.createElement("script"),
            scriptTag = document.getElementsByTagName("script")[0];

        scriptElement.async = true;
        scriptElement.src = 'https://embed.tawk.to/577c2baae1416e7e7c59cbf4/default';
        scriptElement.charset = 'UTF-8';
        scriptElement.setAttribute('crossorigin', '*');
        scriptTag.parentNode.insertBefore(scriptElement, scriptTag);
        // Edn of Tawk.to script.

    }); // end of document ready
})(jQuery); // end of jQuery name space