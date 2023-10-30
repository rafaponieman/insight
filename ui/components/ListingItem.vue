<template>
  <template v-if="column.type === undefined || column.type === 'text'">
    {{ item[column.name] }}
  </template>
  <template v-else-if="column.type === 'date'">
    {{ new Date(item[column.name]).toString() }}
  </template>
  <template v-else-if="column.type === 'additional'">
    <NuxtLink :to="itemLink.to" class="text-purple-300 hover:text-purple-500">{{ itemLink.label }}</NuxtLink>
  </template>
  <template v-else-if="column.type === 'custom'">
    <slot name="custom-column"></slot>
  </template>
</template>

<script setup>
  const props = defineProps({
    additionalData: Object,
    column: Object,
    index: Number,
    item: Object
  })

  const itemLink = computed(() => props.additionalData?.linkData(props.item))
</script>
