(function () {
  "use strict";

  const qAlerts = document.querySelector(".area-alerts");

  qAlerts.addEventListener("click", function (e) {
    if (e.target.matches(".msg-alert .btn-close")) {
      let thisAlert = e.target.parentElement;
      thisAlert.classList.add("hidden");

      // Perform a fade out transition before removing the alert
      thisAlert.addEventListener(
        "transitionend",
        function (e) {
          if (e.propertyName === "opacity") {
            e.target.remove();

            // Delete the container once all messages are dismissed
            if (qAlerts.childElementCount === 0) {
              qAlerts.remove();
            }
          }
        },
        { once: true }
      );
    }
  });
})();
