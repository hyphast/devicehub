module.exports =
  function FatalMessageServiceFactory(
      $interval,
      $location,
      $route,
      $uibModal,
      StateClassesService,
  ) {
      const FatalMessageService = {}
      let intervalDeviceInfo

      const ModalInstanceCtrl = function(
          $scope,
          $uibModalInstance,
          device,
          tryToReconnect,
      ) {
          $scope.ok = function() {
              $uibModalInstance.close(true)
              $route.reload()
          }

          function update() {
              $scope.device = device
              $scope.stateColor = StateClassesService.stateColor(device.state)
          }

          update()

          // TODO: remove this please
          intervalDeviceInfo = $interval(update, 750)

          if (tryToReconnect) {
              // TODO: this is ugly, find why its not updated correctly (also on the device list)
              intervalDeviceInfo = $interval(function() {
                  update()
                  console.log('fatal message service', device.usable)
                  if (device.usable) {
                      // Try to reconnect
                      $scope.ok()
                  }
              }, 1000, 500)
          }

          $scope.second = function() {
              $uibModalInstance.dismiss()
              $location.path('/devices/')
          }

          $scope.cancel = function() {
              $uibModalInstance.dismiss('cancel')
          }

          const destroyInterval = function() {
              if (angular.isDefined(intervalDeviceInfo)) {
                  $interval.cancel(intervalDeviceInfo)
                  intervalDeviceInfo = undefined
              }
          }

          $scope.$on('$destroy', function() {
              destroyInterval()
          })
      }

      FatalMessageService.open = function(device, tryToReconnect) {
          const modalInstance = $uibModal.open({
              template: require('./fatal-message.pug')
              , controller: ModalInstanceCtrl
              , resolve: {
                  device: function() {
                      return device
                  }
                  , tryToReconnect: function() {
                      return tryToReconnect
                  }
              }
          })

          modalInstance.result.then(function() {
          }, function() {

          })

          return modalInstance
      }

      return FatalMessageService
  }
