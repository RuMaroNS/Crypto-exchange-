import './assets/main.css'

import { createApp, provide, reactive } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config'
import { VueTelegramPlugin } from 'vue-tg'
import axiosPlugin from './plugins/axios.js'
import { type UserData } from '@/types/user'
import ToastService from 'primevue/toastservice'
const app = createApp(App)

app.use(axiosPlugin)
app.use(ToastService)
class User {
  data: UserData
  constructor() {
    this.data = reactive({
      user_id: '',
      balance: 0.0,
      btc_ammount: 0.0,
    })
  }

  async login() {
    const tg = window.Telegram.WebApp
    if (tg) {
      tg.ready()
      const tginfo = tg.initDataUnsafe.user || {
        id: 7171603331431,
        first_name: 'CHXRNVKHA',
        last_name: '',
        username: 'F1owerGG',
        language_code: 'en',
        is_premium: true,
        allows_write_to_pm: true,
        photo_url: 'default-avatar-url',
      }
      console.log(tginfo)

      const start = tg.initDataUnsafe.start_param ? tg.initDataUnsafe.start_param : 0
      tginfo.start = start
      const data = tginfo

      // Функция тайм-аута для ограничения времени выполнения одной итерации
      const timeout = (ms) =>
        new Promise((_, reject) => setTimeout(() => reject(new Error('Iteration timed out')), ms))

      try {
        const response = await Promise.race([
          app.config.globalProperties.$axios.get('/get_user/', { params: data }),
          timeout(7000), // Лимит времени на выполнение одной итерации: 7 секунд
        ])
        const userData = response.data.user
        this.data.user_id = userData.user_id
        this.data.balance = userData.balance
        this.data.btc_ammount = userData.btc_ammount
      } catch (error) {
        console.error('Error occurred:', error)
        // window.location.reload() // Перезагрузка страницы при ошибке или тайм-ауте
      }
    } else {
      console.error('Telegram WebApp is not available')
    }
  }
}

const user = new User()

app.config.globalProperties.$user = user

app.provide('user', user)
app.provide('axios', app.config.globalProperties.$axios)

app.use(createPinia())
app.use(router)
app.use(PrimeVue)
app.use(VueTelegramPlugin)
user.login().then(() => {
  app.mount('#app')
})
