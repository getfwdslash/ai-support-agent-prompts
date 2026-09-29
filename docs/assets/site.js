document.querySelectorAll('pre').forEach(function(pre){
  var b=document.createElement('button');b.className='copy';b.type='button';b.textContent='Copy';
  b.addEventListener('click',function(){
    var t=pre.querySelector('code').innerText;
    navigator.clipboard.writeText(t).then(function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy'},1600)});
  });
  pre.appendChild(b);
});
document.querySelectorAll('.content table').forEach(function(t){
  var w=document.createElement('div');w.className='table-wrap';t.parentNode.insertBefore(w,t);w.appendChild(t);
});
