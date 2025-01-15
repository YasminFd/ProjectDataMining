// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
      "pageLength": 5,  // Number of entries per page
      "lengthMenu": [5, 10, 25, 50, 100]  // Options for number of entries
  });
});
