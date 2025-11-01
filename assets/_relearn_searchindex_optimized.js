{{- $pages := slice }}
{{- range .Site.Pages }}
  {{- if partial "_relearn/pageIsSpecial.gotmpl" . }}
  {{- else if and .Title .RelPermalink (or (ne .Site.Params.disableSearchHiddenPages true) (not (partial "_relearn/pageIsHiddenSelfOrAncestor.gotmpl" (dict "page" . "to" .Site.Home) .Path .Site.Home.Path) ) ) }}
    {{- $tags := slice }}
    {{- range .GetTerms "tags" }}
      {{- $tags = $tags | append (partial "title.gotmpl" (dict "page" .Page "linkTitle" true) | plainify) }}
    {{- end }}
    {{- /* Truncate content and description to reduce index size */}}
    {{- $description := or .Description .Summary | plainify | htmlUnescape | truncate 150 }}
    {{- $content := .Plain | htmlUnescape | truncate 300 }}
    {{- /* Skip pages with minimal content */}}
    {{- if gt (len .Plain) 50 }}
      {{- $pages = $pages | append (dict
        "uri" (partial "permalink.gotmpl" (dict "to" .))
        "title" (partial "title.gotmpl" (dict "page" .) | plainify)
        "tags" $tags
        "breadcrumb" (trim (partial "breadcrumbs.html" (dict "page" . "dirOnly" true) | plainify | htmlUnescape) "\n\r\t ")
        "description" (trim $description "\n\r\t " )
        "content" (trim $content "\n\r\t ")
      ) }}
    {{- end }}
  {{- end }}
{{- end -}}
var relearn_searchindex = {{ $pages | jsonify }}