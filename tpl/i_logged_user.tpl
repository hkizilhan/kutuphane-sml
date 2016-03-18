<link rel="stylesheet" href="static/bootstrap.min.css">
<link rel="stylesheet" href="static/style.css">

<script src="/static/jquery-2.2.2.min.js"></script>
<script src="/static/bootstrap.min.js"></script>



<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      
      <span class="navbar-text">Kullanıcı: </span>
      <span class="navbar-brand">{{ get('user_full_name', 'USER_ERROR') }} </span>
      <span class="navbar-text"><a href="/logout">Çıkış</a></span>
    
    </div>
    
    %if is_admin:

    <ul class="nav navbar-nav navbar-right"> 
		
        <li class="dropdown"> 
            <a href="#" class="navbar-brand" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                Yönetici İçin: 
                <span class="caret"></span></a> 
                <ul class="dropdown-menu"> 
                    <li>
                        <a href="/odunctekiler">Ödünçteki Kitapları Listele</a>
                    </li> 
                    <li>
                        <a href="#">Link</a>
                    </li> 
                    <li>
                        <a href="#">Link</a>
                    </li>
                    <li role="separator" class="divider">
                    </li> 
                    <li>
                        <a href="#">Link</a>
                    </li> 
                    <li role="separator" class="divider">
                    </li> 
                    <li>
                        <a href="/update_users">Kullanıcıları Güncelle</a>
                    </li> 
                </ul> 
        </li>
        
        
        
<!--
        <li><span class="navbar-brand">Yönetici İçin:</span></li>
		<li><span class="navbar-text"><a href="/odunctekiler">Ödünçteki Kitapları Listele</a></span></li>
        <li><span class="navbar-text"><a href="/update_users">Kullanıcıları Güncelle</a></span></li>
-->
    </ul>
    
    %end

  </div>
</nav>





