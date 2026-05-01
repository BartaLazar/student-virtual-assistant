let eventGuid = 0
let todayStr = new Date().toISOString().replace(/T.*$/, '') // YYYY-MM-DD of today

export const INITIAL_EVENTS = [
  {
    id: createEventId(),
    title: 'Evénement du jour',
    start: '2023-01-12'
  },
  // {
  //   id: createEventId(),
  //   title: 'hello',
  //   start: '2023-01-12' + 'T12:00:00',
  //   end: '2023-01-12' + 'T13:00:00'
  // }
]

export function createEventId() {
  return String(eventGuid++)
}