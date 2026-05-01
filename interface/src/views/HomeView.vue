<template>
  <div class="home">
    <img class="logo" src="../assets/unigelogo2.png" alt="unige logo">
    <p>Assistant virtuel de l'étudiant </p>
    <br>
    <br>
    <div class="buttons">
        <router-link to="/login"><button class="btnlogin"  @click="submit">Se connecter</button></router-link>
        <br>
        <router-link to="/signup"><button class="btnsignup"  @click="submit">S'enregistrer</button></router-link>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'HomeView',
  created() {
    document.body.style.backgroundColor = "#d80669";
  },
}
</script>
<style>
.home{
  align-items:center;
  text-align: center;
}

.logo{
  margin: auto;
  width:400px;
  
}
p{
  color:white;
  font-size: 40px;
}
.btnlogin {
  background-color:white ;
  border: 3px;
  border-radius: 3px;
  color:black;
  height:35px;
  width:50%;
  margin:auto;
  font-size:100%;
  margin-top:20px;
}
.btnsignup{
  background-color:white ;
  border: 3px;
  border-radius: 3px;
  color:black;
  height:35px;
  width:50%;
  margin:auto;
  font-size:100%;
  margin-top:20px;
}
.buttons {
  border:none;
  width: 50%;
  height: 200px;
  
  margin: auto;
}


</style>
