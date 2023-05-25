$(document).ready(function(){
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();

	//Modify value id user submit
	
	

	// Select/Deselect checkboxes All
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		//Si se selecciona accede a todos los checkbox y los pone en True
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;
				alert("Se seleccionaron todos los elementos");
				//Aca puede acceder a otro valor del checkbox y agregarlo a una lista
				//........                       
			});
		} 
		else{
			//Si esta en falso accede a todos los checkbox y los pone en False
			checkbox.each(function(){
				this.checked = false;                        
			});
		} 
	});

	//Select/Deselect checkbox Individual
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
});