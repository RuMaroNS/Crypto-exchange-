<!--App.vue-->
<template>
  <div class="app">
    <RouterView />
    <NavBar v-if="navbar.isOpen" />
  </div>
</template>

<script setup lang="ts">
import { RouterView, useRoute } from 'vue-router'
import { computed, onMounted, ref, watch } from 'vue'
import { useWebApp, useWebAppViewport, useWebAppSettingsButton } from 'vue-tg'
import NavBar from '@/components/NavBar.vue'
import { useNavbarStore } from './stores/navbarStore'
import router from './router'

// Stores
const navbar = useNavbarStore()
const route = useRoute()

const isFirstLoad = ref(true)
// Telegram Setup
const telegram_app = useWebApp()
const viewport = useWebAppViewport()

const platform = computed(() => telegram_app.platform)

const { onSettingsButtonClicked, showSettingsButton } = useWebAppSettingsButton()

const initializeTelegram = () => {
  telegram_app.ready()

  viewport.expand()

  if (platform.value) {
    window.document.body.setAttribute('platform', platform.value)
  }

  showSettingsButton()
}

// Lifecycle
onMounted(() => {
  initializeTelegram()

  if (isFirstLoad.value) {
    router.push('/exchange')
    isFirstLoad.value = false
  }
})

onSettingsButtonClicked(() => {
  router.push({ path: '/settings' })
})

watch(
  () => route.path,
  (newPath) => {
    const visibleRoutes = ['/', '/stats', '/exchange', '/news']
    const hiddenRoutes = ['/deposit-form', '/deposit/receipt', '/deposit/receipt-attachment']

    if (hiddenRoutes.some((route) => newPath.startsWith(route))) {
      navbar.setIsOpen(false)
    } else {
      navbar.setIsOpen(visibleRoutes.includes(newPath))
    }
  },
)
// Route watcher
</script>

<style scoped>
.app {
  height: var(--tg-viewport-height);
  max-width: 640px;
  margin-left: auto;
  margin-right: auto;
  position: relative;
}
</style>
