<template>
    <div class='demo-app'>
      <div class='demo-app-sidebar' style=" background-color:pink;">
        <div class='demo-app-sidebar-section'>
          <h2>Instructions</h2>
          <ul>
            <li> Selectionnez une date pour ajouter un événement</li>
            <!-- <li>Drag, drop, and resize events</li> -->
            <li>Appuyez sur un événement pour le supprimer</li>
          </ul>
        </div>
        <div class='demo-app-sidebar-section'>
          <label>
            <input
              type='checkbox'
              :checked='calendarOptions.weekends'
              @change='handleWeekendsToggle'
            />
            Avec weekend
          </label>
        </div>
        <div style=" background-color:pink;" class='demo-app-sidebar-section'>
          <h2>Tous les evénements ({{ currentEvents.length }})</h2>
          <ul>
            <li v-for='event in currentEvents' :key='event.id'>
              <b>{{ event.startStr }}</b>
              <i>{{ event.title }}</i>
            </li>
          </ul>
        </div>
      </div>
      <div class='demo-app-main'>
        <FullCalendar
          class='demo-app-calendar'
          :options='calendarOptions'
        >
          <template v-slot:eventContent='arg'>
            <b>{{ arg.timeText }}</b>
            <i>{{ arg.event.title }}</i>
          </template>
        </FullCalendar>
      </div>
    </div>
  </template>

<script>
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import { INITIAL_EVENTS, createEventId } from '@/event-utils'
import esLocale from '@fullcalendar/core/locales/es';
import frLocale from '@fullcalendar/core/locales/fr';

export default({
    components : {
        FullCalendar,
    },
    data() {
        return {
            calendarOptions: {
                plugins: [
                dayGridPlugin,
                timeGridPlugin,
                interactionPlugin // needed for dateClick
                ],
                locales: [ esLocale, frLocale ],
                locale: 'fr',
                headerToolbar: {
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth,timeGridWeek,timeGridDay'
                },
                initialView: 'dayGridMonth',
                initialEvents: INITIAL_EVENTS, // alternatively, use the `events` setting to fetch from a feed
                editable: true,
                selectable: true,
                selectMirror: true,
                dayMaxEvents: true,
                weekends: true,
                select: this.handleDateSelect,
                eventClick: this.handleEventClick,
                eventsSet: this.handleEvents
                /* you can update a remote database when these fire:
                eventAdd:
                eventChange:
                eventRemove:
                */
            },
            currentEvents: [],
        }
    },
    methods: {
        handleWeekendsToggle() {
            this.calendarOptions.weekends = !this.calendarOptions.weekends // update a property
        },
        handleDateSelect(selectInfo) { //here i have to link it to the button add event 
            let title = prompt('Please enter a new title for your event')
            alert(selectInfo.startStr)
            let calendarApi = selectInfo.view.calendar
            calendarApi.unselect() // clear date selection
            if (title) {
                calendarApi.addEvent({
                id: createEventId(),
                title,
                start: selectInfo.startStr,
                end: selectInfo.endStr,
                allDay: selectInfo.allDay
                })
            }
        },
        handleEventClick(clickInfo) {
            if (confirm(`Are you sure you want to delete the event '${clickInfo.event.title}'`)) {
                clickInfo.event.remove()
                //ici on clique sur un event et on va sur une page 
            }
        },
        handleEvents(events) {
            this.currentEvents = events
        },
        }
    
})
</script>

<style lang='css'>
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
    height: 100vh;
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
    max-width: 1100px;
    margin: 0 auto;
  }

  </style>
