<template>
  <section class="bg-gray-50 dark:bg-gray-900">
    <section-header title="Seekers" />
    <listing
      :columns="columns"
      :data="listingData"
      :additional="additional"
    />
  </section>
</template>

<script setup>
  const config = useRuntimeConfig()

  const { data: listingData } = await useFetch(`${config.public.apiRoot}/seekers/`)

  const columns = [
    { name: 'id', label: 'ID' },
    { name: 'name', label: 'Name' },
    { name: 'created', label: 'Created', type: 'date' },
    { name : 'runs', label: 'Runs', type: 'additional'}
  ]

  const additional = [
    { label: '3', linkData: (seeker) => ({ to: `/seekers/${seeker.id}/runs`, label: 'View runs'}) }
  ]
</script>
