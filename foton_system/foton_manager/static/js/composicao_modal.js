// static/js/composicao_modal.js
$(document).ready(function() {
    $('#composicaoModal').on('show.bs.modal', function(event) {
      var button = $(event.relatedTarget);
      var composicaoId = button.data('composicao-id');
      
      $.ajax({
        url: '/orcamento/composicao/modal/' + composicaoId,
        type: 'GET',
        success: function(data) {
          $('#composicaoModal .modal-body').html(data);
        }
      });
    });
  });
  