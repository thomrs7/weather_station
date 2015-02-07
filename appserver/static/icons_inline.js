
// Translations for en_US
i18n_register({"plural": function(n) { return n == 1 ? 0 : 1; }, "catalog": {}});


require([
    'underscore',
    'jquery',
    'splunkjs/mvc',
    'splunkjs/mvc/tableview',
    'splunkjs/mvc/simplexml/ready!'
], function(_, $, mvc, TableView) {

    var firstRow = $('.dashboard-row:eq( 1 )');

    var panelCells = $(firstRow).children('.dashboard-cell');

    $(panelCells[0]).css('width', '80%');
    $(panelCells[1]).css('width', '20%');

    $(window).trigger('resize');


    var IconRenderer = TableView.BaseCellRenderer.extend({
        canRender: function(cell) {
	//console.log(cell);
	return cell.field === 'icon';
        },
        render: function($td, cell) {


	    $td.html(_.template('<img src="<%- icon %>" heigth=45 title="ToolTip" /> ', {
                     icon: cell.value
            }));
           
        }
    });


//         $td.addClass('icon-inline numeric').html(_.template('<%- text %> <i class="icon-<%-icon%>"></i>', {
  //              icon: icon,
    //            text: cell.value
      //      }));

    mvc.Components.get('table1').getVisualization(function(tableView){


        // Register custom cell renderer
        tableView.table.addCellRenderer(new IconRenderer());

	console.log("add renderers");

    });

});


