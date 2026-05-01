<template>
    <div class="calendar">
        <NavBar2/>
       <div class="buttonsadd">
            <router-link to="/event" tag="button"><button class="addeven" @click="submit">Ajouter un événement</button></router-link>
            <router-link to="/task" tag="button"><button class="addtask" @click="submit">Ajouter une tâche </button></router-link>
            <router-link to="/modif" tag="button"><button class="addeven" @click="submit">Modifier une séance</button></router-link>
            <router-link to="/addvac" tag="button"><button class="addeven" @click="submit">Ajouter des vacances</button></router-link>
        </div>
        <Calendar/>
    </div>
</template>
  
<script>
    // @ is an alias to /src
    import NavBar2 from '@/components/NavBar2.vue';
    import Calendar from '@/components/Calendar.vue';
    //import FullCalendar from '@fullcalendar/vue3'
    //import dayGridPlugin from '@fullcalendar/daygrid'
    //import timeGridPlugin from '@fullcalendar/timegrid'
    //import interactionPlugin from '@fullcalendar/interaction'
    //import { INITIAL_EVENTS, createEventId } from '@/event-utils'
    export default ({
        name: 'CalendarView',
        components: {
        NavBar2, 
        Calendar

        },    
})
    
    
    

  </script>
  <style>
    body, html {
        padding: 0;
        margin: 0;
        width: 100%;
        min-height: 100vh;
    }
    .uperdiv{
        height:38px ;
        width:100%;
        background-color:lightgray;
    }
    .cours{
        color:#d80669;
        font-size:25px;
        margin:auto;
        float:left;
        margin-left:13px;
    }
    .actionscal{
        background-color:aqua;
        height: 20%;
        width:100%;
        overflow: scroll;
    }
    
    .buttonsadd{
        float:right;
        margin-right:10px;
        
    }
    .addeven{
        background-color:#d80669;
        color:white;
        border-radius: 3px;
        border:0.5px solid ;
        height: 30px;
        width: 180px;
        margin:15px;
    }
    .addtask{
        background-color:#d80669;
        color:white;
        border-radius: 3px;
        border:0.5px solid ;
        height: 30px;
        width: 180px;
        margin:15px;
    }
   
    .taskliste{
        background-color: #d80669;
        width:35%;
        height: 100vh;
        float: right;

    }
    h2 {
    margin: 0;
    font-size: 16px;
  }
  ul {
    margin: 0;
    padding: 0 0 0 1.5em;
  }
  li {
    margin: 1.5em 0;
    padding: 0;
  }
  b { /* used for event dates/times */
    margin-right: 3px;
  }
  .demo-app {
    display: flex;
    min-height: 100%;
    font-family: Arial, Helvetica Neue, Helvetica, sans-serif;
    font-size: 14px;
  }
  .demo-app-sidebar {
    width: 300px;
    line-height: 1.5;
    background: #eaf9ff;
    border-right: 1px solid #d3e2e8;
  }
  .demo-app-sidebar-section {
    padding: 2em;
  }
  .demo-app-main {
    flex-grow: 1;
    padding: 3em;
  }
  .fc { /* the calendar root */
    /* max-width: 1100px; */
    max-width: 100%;
    margin: 0 auto;
    
  }
  .fc .fc-button-primary:disabled {
    background-color:#d80669;
    border-color:#d80669;
    color: var(--fc-button-text-color);
  } 
  .fc .fc-button-primary {
    background-color:#d80669;
    border-color:#d80669;
    color: var(--fc-button-text-color);
}
.fc .fc-button-primary:not(:disabled).fc-button-active, .fc .fc-button-primary:not(:disabled):active {
  background-color:#d80669;
    border-color:#d80669;
    color: var(--fc-button-text-color);
}
.fc .fc-button-primary:not(:disabled).fc-button-active, .fc .fc-button-primary:not(:disabled):active:hover {
  background-color:#ae0654;
  border-color:#b10555;
    color: var(--fc-button-text-color);
}
.fc .fc-button-primary:not(:disabled).fc-button-active, .fc .fc-button-primary:not(:disabled):hover {
  background-color:#ae0654;
  border-color:#b10555;
    color: var(--fc-button-text-color);
}
a {
    color: var(--bs-link-color);
    /* text-decoration: underline; */
}
  </style>
  