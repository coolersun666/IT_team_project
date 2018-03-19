$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/manicurer/hotest/', {Picture_name: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});


$(selector).css('background-image','url(imgPath)');

