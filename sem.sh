<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Semgrep</title>
    <link rel="icon" href="/favicon.ico?v1" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <link rel="apple-touch-icon" href="/logo192.png" />
    <link rel="manifest" href="/manifest.json" />
    <script nonce="3637b8d900e54155719a1adb2ea96a1b" type="module" crossorigin src="/static/index-BaWJVBjn.js"></script>
    <link rel="modulepreload" crossorigin href="/static/lodash-DQNbFqmc.js">
    <link rel="modulepreload" crossorigin href="/static/monacoReact-jO6nPTf0.js">
    <link rel="modulepreload" crossorigin href="/static/monacoEditor-DIjVdOrs.js">
    <link rel="modulepreload" crossorigin href="/static/monacoLang-Cmn1pRQF.js">
    <link rel="modulepreload" crossorigin href="/static/monacoYaml-CxrrsxPP.js">
    <link rel="stylesheet" crossorigin href="/static/monacoEditor-CNVI1nRY.css">
    <link rel="stylesheet" crossorigin href="/static/monacoLang-CZuaPSry.css">
    <link rel="stylesheet" crossorigin href="/static/index-C0XVb5sm.css">
  </head>
  <body>
    <script nonce="3637b8d900e54155719a1adb2ea96a1b">
      // required for react-joyride
      if (global === undefined) {
        var global = window;
      }
    </script>

    <!-- Google Tag Manager -->
    <script nonce="3637b8d900e54155719a1adb2ea96a1b">
      (function (w, d, s, l, i) {
        w[l] = w[l] || [];
        w[l].push({ "gtm.start": new Date().getTime(), event: "gtm.js" });
        var f = d.getElementsByTagName(s)[0],
          j = d.createElement(s),
          dl = l != "dataLayer" ? "&l=" + l : "";
        j.async = true;
        j.defer = true;
        j.src = "https://www.googletagmanager.com/gtm.js?id=" + i + dl;
        var n = d.querySelector("[nonce]");
        n && j.setAttribute("nonce", n.nonce || n.getAttribute("nonce"));
        f.parentNode.insertBefore(j, f);
      })(window, document, "script", "dataLayer", "GTM-WSN4QTD");
    </script>
    <!-- End Google Tag Manager -->

    <!-- Sign in with Google client -->
    <!-- nosemgrep -->
    <script nonce="3637b8d900e54155719a1adb2ea96a1b" src="https://accounts.google.com/gsi/client" async defer></script>
    <!-- End Sign in with Google client -->
    <!-- Fullstory -->
    <script nonce="3637b8d900e54155719a1adb2ea96a1b">
      var hostname =
        window.location && window.location.hostname !== "localhost"
          ? window.location.hostname
          : "semgrep.dev";
      window["_fs_host"] = hostname + "/fs";
      window["_fs_script"] = hostname + "/fs/s/fs.js";
      window["_fs_org"] = "S99QT";
      window["_fs_namespace"] = "FS";
      !(function (m, n, e, t, l, o, g, y) {
        var s,
          f,
          a = (function (h) {
            return (
              !(h in m) ||
              (m.console &&
                m.console.log &&
                m.console.log(
                  'FullStory namespace conflict. Please set window["_fs_namespace"].'
                ),
              !1)
            );
          })(e);
        function p(b) {
          var h,
            d = [];
          function j() {
            h &&
              (d.forEach(function (b) {
                var d;
                try {
                  d = b[h[0]] && b[h[0]](h[1]);
                } catch (h) {
                  return void (b[3] && b[3](h));
                }
                d && d.then ? d.then(b[2], b[3]) : b[2] && b[2](d);
              }),
              (d.length = 0));
          }
          function r(b) {
            return function (d) {
              h || ((h = [b, d]), j());
            };
          }
          return (
            b(r(0), r(1)),
            {
              then: function (b, h) {
                return p(function (r, i) {
                  d.push([b, h, r, i]), j();
                });
              },
            }
          );
        }
        a &&
          ((g = m[e] =
            (function () {
              var b = function (b, d, j, r) {
                function i(i, c) {
                  h(b, d, j, i, c, r);
                }
                r = r || 2;
                var c,
                  u = /Async$/;
                return u.test(b)
                  ? ((b = b.replace(u, "")),
                    "function" == typeof Promise ? new Promise(i) : p(i))
                  : h(b, d, j, c, c, r);
              };
              function h(h, d, j, r, i, c) {
                return b._api
                  ? b._api(h, d, j, r, i, c)
                  : (b.q && b.q.push([h, d, j, r, i, c]), null);
              }
              return (b.q = []), b;
            })()),
          (y = function (b) {
            function h(h) {
              "function" == typeof h[4] && h[4](new Error(b));
            }
            var d = g.q;
            if (d) {
              for (var j = 0; j < d.length; j++) h(d[j]);
              (d.length = 0), (d.push = h);
            }
          }),
          (function () {
            ((o = n.createElement(t)).async = !0),
              (o.crossOrigin = "anonymous"),
              (o.src = "https://" + l),
              (o.onerror = function () {
                y("Error loading " + l);
              });
            var b = n.getElementsByTagName(t)[0];
            b && b.parentNode
              ? b.parentNode.insertBefore(o, b)
              : n.head.appendChild(o);
          })(),
          (function () {
            function b() {}
            function h(b, h, d) {
              g(b, h, d, 1);
            }
            function d(b, d, j) {
              h("setProperties", { type: b, properties: d }, j);
            }
            function j(b, h) {
              d("user", b, h);
            }
            function r(b, h, d) {
              j(
                {
                  uid: b,
                },
                d
              ),
                h && j(h, d);
            }
            (g.identify = r),
              (g.setUserVars = j),
              (g.identifyAccount = b),
              (g.clearUserCookie = b),
              (g.setVars = d),
              (g.event = function (b, d, j) {
                h(
                  "trackEvent",
                  {
                    name: b,
                    properties: d,
                  },
                  j
                );
              }),
              (g.anonymize = function () {
                r(!1);
              }),
              (g.shutdown = function () {
                h("shutdown");
              }),
              (g.restart = function () {
                h("restart");
              }),
              (g.log = function (b, d) {
                h("log", { level: b, msg: d });
              }),
              (g.consent = function (b) {
                h("setIdentity", { consent: !arguments.length || b });
              });
          })(),
          (s = "fetch"),
          (f = "XMLHttpRequest"),
          (g._w = {}),
          (g._w[f] = m[f]),
          (g._w[s] = m[s]),
          m[s] &&
            (m[s] = function () {
              return g._w[s].apply(this, arguments);
            }),
          (g._v = "2.0.0"));
      })(window, document, window._fs_namespace, "script", window._fs_script);
    </script>
    <!-- End Fullstory -->
    <!-- Google Tag Manager (noscript) -->
    <noscript>
      <iframe
        src="https://www.googletagmanager.com/ns.html?id=GTM-WSN4QTD"
        height="0"
        width="0"
        style="display: none; visibility: hidden"
      ></iframe>
    </noscript>
    <!-- End Google Tag Manager (noscript) -->
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!-- nosemgrep -->
    <script nonce="3637b8d900e54155719a1adb2ea96a1b"
      src="https://snjdw73vnmhs.statuspage.io/embed/script.js"
      async
      defer
    ></script>
    <!-- nosemgrep -->
    <script nonce="3637b8d900e54155719a1adb2ea96a1b"
      type="module"
      src="https://interfaces.zapier.com/assets/web-components/zapier-interfaces/zapier-interfaces.esm.js"
      async
      defer
    ></script>
  </body>
</html>
