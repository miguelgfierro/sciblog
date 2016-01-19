(function() {
  var djangoJQuery;
  if (typeof jQuery == 'undefined' && typeof django == 'undefined') {
    console.error('ERROR django-ckeditor missing jQuery. Set CKEDITOR_JQUERY_URL or provide jQuery in the template.');
  } else if (typeof django != 'undefined') {
    djangoJQuery = django.jQuery;
  }

  var $ = jQuery || djangoJQuery;
  $(function() {
    initialiseCKEditor();
    initialiseCKEditorInInlinedForms();

    function initialiseCKEditorInInlinedForms() {
      try {
        $(document).on("click", ".add-row a, .grp-add-handler", function () {
          initialiseCKEditor();
          return true;
        });
      } catch (e) {
        $(document).delegate(".add-row a, .grp-add-handler", "click",  function () {
          initialiseCKEditor();
          return true;
        });
      }
    }

    function initialiseCKEditor() {
      $('textarea[data-type=ckeditortype]').each(function(){
        if($(this).data('processed') == "0" && $(this).attr('id').indexOf('__prefix__') == -1){
          $(this).data('processed',"1");
          $($(this).data('external-plugin-resources')).each(function(){
              CKEDITOR.plugins.addExternal(this[0], this[1], this[2]);
          });
          console.log("$(this).attr('id')=",$(this).attr('id'));
          console.log("$(this).data('config')=",$(this).data('config'));
          //CKEDITOR.replace($(this).attr('id'), $(this).data('config'));
          CKEDITOR.replace( $(this).attr('id'), {
			extraPlugins: 'embed,autoembed,image,image2,mathjax,uploadimage,uploadwidget,filetools,widget,clipboard,notification,notificationaggregator,button,toolbar,codesnippet',
			height: 500,

			// Format (I removed h1,h2,h3 because they are already included in the template)
			format_tags: 'p;h4;h5;h6;div',
			format_h4 : { element: 'h4', attributes: { 'class': 'section' } },
			format_h5 : { element: 'h5', attributes: { 'class': 'subsection' } },
			format_h6 : { element: 'h6', attributes: { 'class': 'subsubsection' } },

			//MATHJAX
			mathJaxLib: 'http://cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML',

			//FILE UPLOADER
			filebrowserBrowseUrl: '/ckeditor/browse/',
            filebrowserUploadUrl: '/ckeditor/upload/',

			// EMBEDED CONTENT
			// The following options are not necessary and are used here for presentation purposes only.
			// They configure the Styles drop-down list and widgets to use classes.
			stylesSet: [
				{ name: 'Narrow image', type: 'widget', widget: 'image', attributes: { 'class': 'image-narrow' } },
				{ name: 'Wide image', type: 'widget', widget: 'image', attributes: { 'class': 'image-wide' } },
				{ name: 'Narrow media', type: 'widget', widget: 'embed', attributes: { 'class': 'embed-narrow' } },
				{ name: 'Centered media', type: 'widget', widget: 'embed', attributes: { 'class': 'embed-align-center' } }
			],
			// Load the default contents.css file plus customizations for this sample.
			contentsCss: [ CKEDITOR.basePath + 'contents.css', 'http://sdk.ckeditor.com/samples/assets/css/widgetstyles.css' ],
			// Configure the Enhanced Image plugin to use classes instead of styles and to disable the
			// resizer (because image size is controlled by widget styles or the image takes maximum
			// 100% of the editor width).
			image2_alignClasses: [ 'image-align-left', 'image-align-center', 'image-align-right' ],
			image2_disableResizer: true
		} );

        }
      });
    }
  });
}());
