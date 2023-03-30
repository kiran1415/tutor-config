<div class="video_news">
  <iframe width="100%" height="100%" src="https://www.youtube.com/embed/y0t3D8hGt4w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

</div>

<ul class="videos_list">
  <li class="active" id="ranjeet" title="ranjeet singh">
<img src="assets/images/ranjeet.jpg" alt="">
    </li>
  <li  id="aswini" title="Aswini Kumar">
<img src="assets/images/aswini.jpg" alt="">
    </li>
  <li  id="ravikumar" title="Ravikumar">
<img src="assets/images/ravikumar.jpg" alt="">
    </li>
</ul>

<script>
$(document).ready(function(){

  var video_trigger = $('.videos_list li'),
      containers = $('.video_news');
    video_trigger.on('click', function(){
      $('.videos_list li').removeClass('active');
    var $this = $(this),
       targets=$(this).attr('id');
    containers.load('partials/' +targets + '.php');
    $(this).addClass('active');
    });
    });

</script>
