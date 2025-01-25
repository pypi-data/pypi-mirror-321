<template>
  <div class="q-pa-md">
    <q-table
      :class="$q.dark.isActive?'my-sticky-header-last-column-table-dark' : 'my-sticky-header-last-column-table'"
      flat
      bordered
      :rows="rows"
      :columns="columns"
      row-key="name"
      :pagination="pagination"
      separator="cell"
      :no-data-label="t('nodata')"
      :rows-per-page-label="t('per_page')"
      :rows-per-page-options="[1,10,30,50,200,0]"
      :table-style="{ height: ScreenHeight, width: ScreenWidth }"
      :card-style="{ backgroundColor: CardBackground }"
      @request="onRequest"

    >
      <template v-slot:top="props">
        <q-btn-group flat>
          <q-btn :label="t('refresh')" icon="refresh" @click="onRequest({'pagination': pagination})" v-show="PermissionCheck('Get User List')">
            <q-tooltip class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">{{ t('refresh') }}</q-tooltip>
          </q-btn>
          <q-btn :label="t('new')" icon="add" v-show="PermissionCheck('Create One User')">
            <q-tooltip class="bg-indigo" :offset="[10, 10]" content-style="font-size: 12px">{{ t('new') }}</q-tooltip>
          </q-btn>
        </q-btn-group>
        {{ pagesNumber }}
        <q-space />
        <q-input borderless dense debounce="300" color="primary" v-model="search" @input="onRequest({'pagination': pagination})" @keyup.enter="onRequest({'pagination': pagination})">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
        <q-btn
          flat round dense
          :icon="props.inFullscreen ? 'fullscreen_exit' : 'fullscreen'"
          @click="props.toggleFullscreen"
        />
      </template>

      <template v-slot:body-cell="props">
        <q-td :props="props">
          <div v-if="props.col.name === 'action'">
            <q-btn round flat icon="admin_panel_settings"></q-btn>
            <q-btn round flat icon="admin_panel_settings"></q-btn>
            <q-btn round flat icon="lock_person" v-show="!props.row.is_active"></q-btn>
            <q-btn round flat icon="lock_open" v-show="props.row.is_active"></q-btn>
            <q-btn round flat icon="delete_sweep"></q-btn>
          </div>
          <div v-else>
            {{ props.value }}
          </div>
        </q-td>
      </template>

      <template v-slot:pagination="scope">
        {{scope}}
        <q-pagination
          v-model="scope.pagination.page"
          :max="scope.pagesNumber"
          input
          input-class="text-orange-10"
          @update:model-value="PageChanged(scope)"
        />
      </template>

    </q-table>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useQuasar } from 'quasar'
import { useI18n } from "vue-i18n"
import { get } from 'boot/axios'
import { useTokenStore } from 'stores/token'

const { t } = useI18n()
const $q = useQuasar()
const tokenStore = useTokenStore()

const columns = computed( () => [
  {
    name: 'username', required: true, label: t('username'), align: 'left', field: 'username' },
  { name: 'email', align: 'center', label: t('email'), field: 'email' },
  { name: 'date_joined', label: t('date_joined'), field: 'date_joined' },
  { name: 'last_login', label: t('last_login'), field: 'last_login' },
  { name: 'updated_time', label: t('updated_time'), field: 'updated_time' },
  { name: 'action', label: t('action'), align: 'right' }
])

const rows = ref( [])

const search = ref( '')

const rowsCount = ref(0)

const pagination  = ref({
    page: 1,
    rowsPerPage: 1,
    rowsNumber: 1
  })

const pagesNumber = computed( () => {
  if (token.value !== '') {
    return Math.ceil(rowsCount.value / pagination.value.rowsPerPage)
  } else {
    return 0
  }
})

const ScreenHeight = ref($q.screen.height * 0.73 + '' + 'px')
const ScreenWidth = ref($q.screen.width * 0.825 + '' + 'px')
const CardBackground = ref($q.dark.isActive? '#121212' : '#ffffff')

const token = computed(() => tokenStore.token)
const userInfo = computed(() => tokenStore.tokenDataGet)

function onRequest (props) {
  if (token.value !== '' && PermissionCheck('Get User List')) {
    get({
      url: 'core/user/',
      params: {
        search: search.value,
        page: props.pagination.page,
        max_page: props.pagination.rowsPerPage,
      }
    }).then(res => {
      rows.value = res.results
      rowsCount.value = res.count
    }).catch(err => {
      console.error(err)
      return Promise.reject(err)
    })
    pagination.value = props.pagination
  }
}

function PageChanged(e) {
  console.log('pageChange', e)
}

function PermissionCheck(e) {
  if (token.value !== '') {
    return e in userInfo.value.permissions;
  } else {
    return false
  }
}

onMounted(() => {
  onRequest({
    pagination: pagination.value
  })
})

watch(() => $q.dark.isActive, val => {
  CardBackground.value = val? '#121212' : '#ffffff'
})

watch(() => pagination.value, val => {
  console.log('watch', val.sortBy)
})

</script>
