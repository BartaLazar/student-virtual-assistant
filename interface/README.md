# Student Virtual Assistant, Frontend

This is the **frontend** of the [Student Virtual Assistant](../README.md): a Vue 3 single-page application that lets a student log in, manage their courses and schedule, and track tasks and revisions. It talks to the Flask backend (see the [root README](../README.md)) over a REST API.

> This folder is part of an archived, academic project. See the [root README](../README.md) for the full project overview, architecture and known limitations.

## Tech stack

- [Vue 3](https://vuejs.org/) (Options API, Vue CLI project)
- [Vue Router](https://router.vuejs.org/) (hash-based routing)
- [Vuex](https://vuex.vuejs.org/) for state management
- [Vuetify](https://vuetifyjs.com/) 3, [Bootstrap](https://getbootstrap.com/)/Bootstrap-Vue, [Semantic UI](https://semantic-ui.com/) for UI components (several UI kits were used across the project)
- [FullCalendar](https://fullcalendar.io/) for the calendar views
- [Axios](https://axios-http.com/) for HTTP requests to the backend

## Prerequisites

- Node.js and npm
- The backend API running and reachable (see [../README.md](../README.md) for how to start it). By default the app expects it at `http://127.0.0.1:5000/`.

## Project setup

Install dependencies:

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

This starts a local dev server (by default at `http://localhost:8080`) with hot-reload.

### Compiles and minifies for production

```
npm run build
```

Outputs a production-ready build to `dist/`.

### Customize configuration

See the [Vue CLI Configuration Reference](https://cli.vuejs.org/config/).

## Pointing the app at a different backend

The backend URL is hardcoded in [`src/common/common.js`](src/common/common.js) as `BASE_PATH`:

```js
export const BASE_PATH = 'http://127.0.0.1:5000/';
```

Edit this value if your backend runs on a different host/port.

## Project structure

```
interface/
├── public/               # Static assets and index.html
├── src/
│   ├── main.js           # App entry point (plugins, icons, mount)
│   ├── App.vue           # Root component
│   ├── router/           # Vue Router route definitions
│   ├── store/            # Vuex store
│   ├── common/           # Shared constants (API base path)
│   ├── event-utils.js    # Calendar/event helper functions
│   ├── plugins/          # Vuetify and webfontloader setup
│   ├── assets/           # Images/logos
│   ├── components/       # Reusable UI components (NavBar, Calendar, lists, toggle button...)
│   └── views/            # Page-level components, one per route (see below)
├── babel.config.js
├── vue.config.js
└── package.json
```

## Pages / routes

| Route         | View                  | Purpose                                    |
|---------------|-----------------------|---------------------------------------------|
| `/`           | `HomeView`            | Landing page                                |
| `/login`      | `LoginView`           | Student login                               |
| `/signup`     | `SignupView`          | Account creation                            |
| `/menu`       | `MenuView`            | Main navigation menu                        |
| `/calendar`   | `CalendarView`        | Full calendar of courses and events         |
| `/day`        | `DayView`             | Single-day schedule view                    |
| `/liste`      | `ListeView`           | List view of tasks/events                   |
| `/event`      | `EventView`           | Event details                               |
| `/task`       | `TaskView`            | Task details                                |
| `/modif`      | `ModifView`           | Edit an existing course/event               |
| `/addvac`     | `AddvacView`          | Declare a holiday/break period              |
| `/courses`    | `CoursesView`         | List of the student's courses               |
| `/lectures`   | `LecturesView`        | Course lecture checklist                    |
| `/experiences`| `ExperiencesView`     | Course experience/seminar checklist         |
| `/exptp`      | `ExpTpView`           | Course TP (practical work) checklist        |
| `/revisions`  | `RevisionsView`       | Course revisions checklist                  |

## Known limitations

- The backend base URL is hardcoded (see above) rather than read from an environment variable.
- Several overlapping UI/calendar libraries are installed (`vue-simple-calendar`, `vue-calendar-3`, `@lbgm/pro-calendar-vue`, FullCalendar...); not all of them are necessarily used in the final views, this is a leftover of iterating on the UI during development.
- As with the rest of the repository, this is an archived school project (Oct-Dec 2022): no automated tests, and some functionality may be incomplete since a few files were removed from the published repo for privacy reasons.

## Further assistance

For questions about the frontend, contact Laila Laaris, Laila.Laaris@unige.ch. See the [root README](../README.md) for full contact info.
