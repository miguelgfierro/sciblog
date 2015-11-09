/* MIT license. José Ignacio Fernández, 2013 */
$('head').append("<style type='text/css'>.container { height: 1133px; } \n #contents { display: none; }</style>");

Layout = {
  new_page: function() {
    var html =
    "<div class='container'>" +
      "<div class='row'>" +
        "<div class='two columns'>&nbsp;</div>" +
        "<div class='six columns content'><div style='margin-bottom: 1rem;'>&nbsp;</div></div>" +
        "<div class='six columns content'><div style='margin-bottom: 1rem;'>&nbsp;</div></div>" +
        "<div class='two columns'>&nbsp;</div>" +
      "</div>" +
    "</div>";
    $(document.body).append(html);
  },
  overflow: function(column, node) {
    var page = column.parents(".container");
    var padding = parseInt(page.css("padding-bottom"));
    return (column.position().top + node.position().top + node.outerHeight() > page.outerHeight() - padding);
  },
  space: function(column, node) {
    var page = column.parents(".container");
    var padding = (page.outerHeight() - page.height()) / 2;
    return (page.outerHeight() - padding) - (column.position().top + node.position().top);
  },
  shift_word: function(node1, node2) {
    var old_html = node1.html();
    var contents = node1.contents();
    var subnode;
    var i = 1;
    do { subnode = contents[contents.length - i++]; } while (subnode.nodeName == '#text' && subnode.nodeValue.trim()=='')

    if (subnode.nodeName == '#text') {
      var words = subnode.nodeValue.split(' ');
      var word = words.pop();
      subnode.nodeValue = words.join(' ');
      node2.prepend(document.createTextNode(word + " "));
    } else {
      node2.prepend(document.createTextNode(" "));
      node2.prepend(subnode);
    }
  },
  render: function(selector) {
    $(".row").show();
    var index = 0;
    $(selector).children().each(function() {
      var column  = $($(".content")[index]);

      column.append($(this));
      if ( Layout.overflow(column, $(this))) {
        if ( $(this).prop("tagName") == "P" &&
             Layout.space(column, $(this)) > 45) {
          var node1 = $(this);
          var node2 = $("<p class='wrap " + node1.attr("class") + "'></p>");
          index ++;
          if (index % 2 == 0) { Layout.new_page(); }
          $($(".content")[index]).append(node2);
          while (Layout.overflow(column, node1) ) {
            Layout.shift_word(node1, node2);
          }
        } else {
          index ++;
          if (index % 2 == 0) { Layout.new_page(); }
          $($(".content")[index]).append($(this));
        }
      }
    });
  }
}
