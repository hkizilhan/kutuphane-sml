<link rel="stylesheet" href="static/bootstrap.min.css">

<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      
      <span class="navbar-text">Kullanıcı: </span>
      <span class="navbar-brand">{{ get('user_full_name', 'USER_ERROR') }} </span>
      <span class="navbar-text"><a href="/logout">Çıkış</a></span>
    
    </div>
    
    %if is_admin:

    <ul class="nav navbar-nav navbar-right"> 
		<li><span class="navbar-brand">Yönetici İçin:</span></li>
		<li><span class="navbar-text"><a href="/update_users">Kullanıcıları Güncelle</a></span></li>
    </ul>
    
    %end

  </div>
</nav>





