

/* Javascript file for handling the office management system functionaliies */

  
	// variable for saving attendence
	var attendence = {};



function loginAlert(message){
		$('#login-popup').fadeIn(10)
				   .addClass('login-popup-show')
			       .removeClass('login-popup-hide')
		$('#popup-layer').addClass('toggle-layer')	
		$('#content').find('#popup-message').text(message);
}
function logoutAlert(heading, message){
		$('#logout-popup').fadeIn(10)
				   .addClass('logout-popup-show')
			       .removeClass('logout-popup-hide')
		$('#popup-layer').addClass('toggle-layer')
		$('#logout-popup').find('#heading').text(heading);	
		$('#logout-popup').find('#popup-message').text(message);
}

function logout(){ 
		$('#logout-popup').removeClass('logout-popup-show');
		$('#logout-popup').addClass('logout-popup-hide');
		$('#logout-popup').fadeOut(450);
		$('#popup-layer').removeClass('toggle-layer');
		}
function open_others(){
		
		$('#dir_submenu').css('display', 'none');
		$('#emp_submenu').css('display', 'none');
		$('#oth_submenu').css('display', 'block');
}
function open_dir(){
		$('#dir_submenu').css('display', 'block');
		$('#emp_submenu').css('display', 'none');
		$('#oth_submenu').css('display', 'none');
}
function open_employee(){
		$('#dir_submenu').css('display', 'none');
		$('#emp_submenu').css('display', 'block');
		$('#oth_submenu').css('display', 'none');
}
function show_dir(){
		  $('#directors').show();	
		  $('#employees').hide();		
		  $('#others').hide(); 
}
function show_emp(){
		  $('#directors').hide();	
		  $('#employees').show();
		  $('#others').hide();	
}
function show_oth(){
		 $('#directors').hide();		
		 $('#employees').hide();	
		 $('#others').show();	
}
 
function time(){
		var today = new Date();
		var mm = today.getMinutes();
		var hh = today.getHours();
		var ss = today.getSeconds();
		var dd = today.getDate();
		var mt = today.getMonth();
		var yy = today.getYear();
		if (hh < 10)hh = '0'+hh;
		if (mm < 10)mm = '0'+mm;
		if (ss < 10)ss = '0'+ss;
		if (mt < 10)mt = '0'+mt;
		if (dd < 10)dd = '0'+dd;
		
		var time = '        ' + hh + ":" + mm +":" + ss;  
		$('#time').text(time);
	}
function setCurUser(){		
		$('#loginuser').text('  ' + sessionStorage.username.toUpperCase());
}
function show_attendence_editor(){
		$('#attendence-editor').show();
}
function hide_attendence_editor(){
		$('#attendence-editor').hide();
}
function mark_attendence(id){
		show_a_editor(id);
		show_atten_btn_panel();
		$('#dis-layer').toggleClass('toggle-layer');
}
function hide_atten_btn_panel(){
		$('#atten-btn-panel').hide();
}
function show_atten_btn_panel(){
		$('#atten-btn-panel').show();
}
function save_attendence(atten_data){    

    $.ajax({
        type: "POST",
        url: '/save_attendence/',
        data: atten_data,
        success: function(result)
        {
            /* The div contains now the updated form */
         $('#dis-layer').toggleClass('toggle-layer');
		 $('#save-message').css('display', 'block');
        }
    });
}
function attendence_selected(){
		
		var emp_att = $('#att-status').val(); 
		var id = $('#name').text() +"-"+ $('#day').text(); 
		$('#' + id).text(emp_att);
		attendence[id] = emp_att;
		$('#att-status').val('-'); 
		$('#attendence-editor').toggleClass('a-editor-tog');
		$('#dis-layer').toggleClass('toggle-layer');
}
function show_a_editor(id){
		$('#attendence-editor').toggleClass('a-editor-tog');
		$('#name').text(id.split('-')[0]);	
		$('#day').text(id.split('-')[1] );
}	
function on_staff_load(){
	    $('#register_dir').click(function(){
			alert('testing list click');
		 });
}

 $(document).ready(function(){    

	  $('#user-login').show();
	  $('#user-login').fadeOut(10);	
      $('#user-input').addClass('user-input');     	      
      $('#login-b').addClass('login-btn');
      $('#user').addClass('input-line');  
      $('#pass').addClass('input-line');
      $('#login').addClass('input-line');
	  $('#oth_submenu').css('display', 'none');
	  $('#emp_submenu').css('display', 'none'); 	 
	  $('#dir_submenu').css('display', 'none');
	  $('#fm_submenu').css('display', 'none');	
	  $('#sw_submenu').css('display', 'none');	
	  $('#directors').hide();
	  $('#others').hide();	
      $('#attendence').hide();	
	  $('.footer').css('width', screen.width);
	  $('.staff-heading').css('width', screen.width);
	  $('.heading-style').css('width', screen.width);
	  time(); 
	  setInterval(time, 1000);
     
	  hide_atten_btn_panel();


	 $('#atten_save').bind('click', function(){
		save_attendence(attendence);
		attendence = {};
		hide_atten_btn_panel();
					
	});

	 $('#atten_cancel').bind('click', function(){
		attendence = {};
		hide_atten_btn_panel();
					
	});
	
	$('#director').bind('click', function(){
		 open_dir();
		 show_dir();
	  });
	$('#employee').bind('click', function(){
		open_employee();
		show_emp();
	});
	$('#other').bind('click', function(){
		open_others();
		show_oth();
	});
	$('#save-ok').bind('click', function(){
		$('#dis-layer').toggleClass('toggle-layer');
		$('#save-message').css('display', 'none');
	});
	$('#closePopupbtn').bind('click', function(){
		$('#login-popup').removeClass('login-popup-show');
		$('#login-popup').addClass('login-popup-hide');
		$('#login-popup').fadeOut(450);
		$('#popup-layer').removeClass('toggle-layer');			
	   });

	$('#logoutPopupCancel').bind('click', function(){
			logout();	
	 });

	$('#logoutPopupOk').bind('click', function(){
		logout();
		window.location.href = 'user/logout';	
	 });
	
	$('#login-form').submit(function(){
		var mess = '';
	 if($('#username').val() == ''&&$('#password').val() == ''){
		 mess = 'Enter username and password';
		loginAlert(mess);	
		return false;
	  }else if($('#username').val() == ''){
			 mess = 'Enter username';
			loginAlert(mess);	
			return false;
		}else if($('#password').val() == ''){
				 mess = 'Enter password';
				loginAlert(mess);	
				return false;
		}
		
		$('#login-form').attr('action', 'main');
		sessionStorage.username =  $('#username').val();
	});	

	 $('a').bind('click', function(){
		  $('#home-page').show();
		  $('#user-login').hide();
	});	 
	  $('#user-login').fadeIn(3000);   
	  $('#login-b').hover(function(){
			$(this).toggleClass('button-hover');	
	}); 

	$('#logout').bind('click', function(){
			logoutAlert('Logout','User logging out..');
	});	
	$('#attend').bind('click', function(){
	 	$('#attendence').show();
		$('#tasks').hide();
	});		      
});
