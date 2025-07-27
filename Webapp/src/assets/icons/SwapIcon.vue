<template>
  <div class="swap-icon" :class="{ 'animate-swap': isAnimating }" @click="handleClick">
    <svg width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path
        class="arrow-up"
        d="M11.1542 0.989594L15.5875 5.42294"
        stroke="white"
        stroke-width="1.5"
        stroke-miterlimit="10"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
      <path
        class="arrow-up"
        d="M11.1542 16.0104V0.989594"
        stroke="white"
        stroke-width="1.5"
        stroke-miterlimit="10"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
      <path
        class="arrow-down"
        d="M5.84575 16.0104L1.41245 11.5771"
        stroke="white"
        stroke-width="1.5"
        stroke-miterlimit="10"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
      <path
        class="arrow-down"
        d="M5.84584 0.989594V16.0104"
        stroke="white"
        stroke-width="1.5"
        stroke-miterlimit="10"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  isAnimating: boolean
}>()

const emit = defineEmits(['click'])

const handleClick = () => {
  emit('click')
}
</script>

<style scoped>
.swap-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 35px;
  height: 35px;
  border-radius: 50%;
  background: linear-gradient(135deg, #7b42f6, #2ea7e0);
  cursor: pointer;
}

.arrow-up,
.arrow-down {
  transition: transform 0.5s ease;
}

.animate-swap .arrow-up {
  animation: moveUp 0.5s ease;
}

.animate-swap .arrow-down {
  animation: moveDown 0.5s ease;
}

@keyframes moveUp {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
    opacity: 0;
  }
  51% {
    transform: translateY(10px);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes moveDown {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(10px);
    opacity: 0;
  }
  51% {
    transform: translateY(-10px);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}
</style>
