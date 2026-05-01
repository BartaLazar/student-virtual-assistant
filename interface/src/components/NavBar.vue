<template>
  <nav class="navbar navbar-expand-lg" id="nav">
      <div class="container-fluid">
      <a href="#" class="navbar-brand">
      <!-- Logo Image -->
      <img src="../assets/logonom.png" width="50" alt="" class="d-inline-block align-middle mr-2"></a>
      <button class="deconexion"  @click="logout" type="submit" v-if="!isLogged">Deconnexion</button>
      </div>
  </nav>  
</template>

<script>
export default {
  name: 'NavBar',
  props: {
  },
  data(){
    return{
        clicked: false,
        clicked2: false,
        isLogged: this.$router.currentRoute.value.name === 'home'|| this.$router.currentRoute.value.name === 'login' || this.$router.currentRoute.value.name === 'signup'?true:false

    }
  },
  
  methods: {
    logout(){
      const route = this.$router;
      alert("logout");
      route.push({ name: 'home' })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  body{
      background-color:white; 
      width:100%;
  }
  .navbar{
    background-color:#d80669;
    position:relative;
    width:100%;
    max-height: 100px;
  }
  nav{
    position: relative;
    top: 0;
    margin:auto;
  }
  img{
    width:120px;
    margin-left:0px;
  }
  .deconexion{
    
    background-color:black;
    width:10%;
    font-size:100%;
    height:35px;
    color:white;
    border:none;
    border-radius: 3px;
  }
  .deconexion:hover{
    background-color:#b90b5c;;
  }
</style>
