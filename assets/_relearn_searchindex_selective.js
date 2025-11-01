{{- $pages := slice }}
{{- range .Site.Pages }}
  {{- $skipPaths := slice "blog/archive" "casebook" "story" }}
  {{- $skip := false }}
  {{- range $skipPaths }}
    {{- if hasPrefix $.RelPermalink . }}
      {{- $skip = true }}
    {{- end }}
  {{- end }}
  
  {{- if partial "_relearn/pageIsSpecial.gotmpl" . }}
  {{- else if $skip }}
    {{- /* Skip heavy content sections */ }}
  {{- else if and .Title .RelPermalink (or (ne .Site.Params.disableSearchHiddenPages true) (not (partial "_relearn/pageIsHiddenSelfOrAncestor.gotmpl" (dict "page" . "to" .Site.Home) .Path .Site.Home.Path) ) ) }}
    {{- $tags := slice }}
    {{- range .GetTerms "tags" }}
      {{- $tags = $tags | append (partial "title.gotmpl" (dict "page" .Page "linkTitle" true) | plainify) }}
    {{- end }}
    {{- /* Only include title, description and first 200 chars of content */}}
    {{- $description := or .Description .Summary | plainify | htmlUnescape | truncate 100 }}
    {{- $content := .Plain | htmlUnescape | truncate 200 }}
    {{- $pages = $pages | append (dict
      "uri" (partial "permalink.gotmpl" (dict "to" .))
      "title" (partial "title.gotmpl" (dict "page" .) | plainify)
      "tags" $tags
      "description" (trim $description "\n\r\t " )
      "content" (trim $content "\n\r\t ")
    ) }}
  {{- end }}
{{- end -}}
var relearn_searchindex = {{ $pages | jsonify }}