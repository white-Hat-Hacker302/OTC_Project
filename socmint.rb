#!/usr/bin/env ruby
# encoding: utf-8
# ============================================================
#  SocMint-Framework v1.0
#  Social Media OSINT & Security Testing Framework
#  Coded by: Cyber Security Engineer Mr Sabaz Ali Khan
#  For AUTHORIZED security assessments only.
# ============================================================
require 'net/http'
require 'uri'
require 'json'
require 'open-uri'
require 'time'

# ---------------- BANNER ----------------
BANNER = <<-'EOF'

     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⢀⣠⣤⣶⣶⣶⣶⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⢀⣀⣀
   ⣠⣾⣿⣿⣿⣿⡔⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣫⣯⣷⣾⣿⣿⣿⣿⣿⣿⣷⣄
  ⣠⣾⣿⣿⣿⣿⣿⣿⣷⡙⢿⣿⣿⣿⣿⣿⣿⡿⢋⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀
  ⢀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⠿⠿⠿⢟⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣄
  ⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡏⠉⠙⢿⣿⣿⣦⡀
  ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⡿⡍⠳⣄⡀⢀⣿⣿⣿⣿⣆
  ⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⢿⡄⠸⡿⢄⠛⣘⢠⣼⣿⣿⣿⣿⣿⣧⡀
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡞⣼⡻⡄⠳⡤⠽⠾⠿⠿⠿⢛⣻⣿⣿⣿⣷⡀
  ⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣄⠙⢶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣧
  ⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⢉⣁⣀⣀⣀⣀⣀⣉⡉⠙⠛⠻⢿⣿⣿⣿⣿⣿⣯⣻⣍⡲⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
  ⡀⣶⣤⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣁⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣈⠛⢿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⡿⠟⠛⠛⠁
  ⣿⣿⣿⣿⣿⣿⣿⣿⣝⢿⣿⣿⣿⣿⣿⣿⣟⣡⣶⠿⢛⣛⣉⣭⣭⣤⣤⡴⠶⠶⠶⠶⢲⣴⣤⠭⠭⡭⣟⠻⠦⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣀⣠⣶⣿⣆
  ⠹⣿⣿⣿⣿⣿⣿⣙⠻⣿⣮⣛⠿⣿⣿⣿⣫⣵⡶⠟⣛⣋⣭⣭⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣮⣽⣿⣿⣿⠿⠟⠛⠉⢀⣴⣿⣿⣿⣿⣿⣿⣶⡀
  ⠈⠙⠋⠁⠀⠈⠉⠛⠳⣭⣛⢷⣦⣸⣿⣯⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⡟⣿⣿⣿⣿⡇
  ⢀⣠⣾⣿⣿⠿⠿⢿⣹⣿⣧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⡏⣀⣴⣾⣿⣿⠿⠛⠉⠀⠀⠀⠈⠛⠛⠉
  ⢴⠿⠛⠋⠁⠀⠀⠀⢀⣯⢿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⠣⣟⡻⠟⠉
  ⢀⣀⣴⣾⣿⠈⡿⣿⠃⠀⠀⠀⠈⠉⠛⠻⠿⣿⣿⣿⣿⣿⠿⠛⠉⠉⠀⠈⠉⠛⣿⣽⡟⠋⠁
  ⣤⣶⣾⣿⣿⣿⣿⣿⣀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⣹⡟⣻⣿⡃⠀⠀⠀⠀⠀⠀⠀⢹⣷⣤⡀
  ⣾⣿⣿⣿⣿⣿⣿⣿⡿⢹⣿⣿⣿⡄⠀⠀⠀⠀⣰⣿⢣⡇⣿⣷⡀⠀⠀⠀⠀⠀⣼⣿⣿⡇
  ⠋⠙⠛⠻⣿⣿⣿⣿⣿⠏⠀⠈⢿⣿⣿⣿⣦⣄⣀⣀⣀⣠⣴⣿⣏⡞⢻⣸⣿⣷⣄⠀⠀⣀⣤⠴⣾⣿⣿⣿⠃
  ⠹⣿⣿⠃⠀⠀⠀⠈⢿⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣶⠾⠋⠁
  ⣏⠀⠀⠀⠀⠀⣀⣼⣿⡛⢿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠟⣡⣾⣆
  ⣶⣿⣿⣯⣿⡇⠀⢹⣿⣿⣿⣿⣷⣤⣤⣦⣶⣿⣿⣿⣿⣿⡇⠀⣿⣿⢸⣿⣶⣤
  ⣄⣠⣴⣾⣿⣟⣿⠟⠁⣿⡇⠀⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⡇⢀⣿⣿⠙⢮⣛⠿⣷⣦⣄⣀⣀⣀⣠⣀
  ⣶⣶⣾⣿⣿⡿⣛⣽⠞⠋⠀⠀⠀⣿⣷⠀⣍⠇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠉⡄⣸⣿⡿⠀⠀⠈⠙⠮⣟⠿⣿⣿⣿⣿⣿⣿⡆
  ⣹⣿⣿⣿⢵⡿⠋⠀⠀⠀⠀⠀⢿⣿⣦⣿⡷⣄⠙⠿⣿⢹⣿⣿⢼⡿⠋⣡⣶⣳⣿⣿⣿⠃⠀⠀⠀⠈⠿⠬⣿⣿⣿⣿⣿⣷
  ⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣷⣻⢿⣶⣬⣈⣉⣉⣤⣴⣿⣻⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡿⠇
  ⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⡇⣿⣇⣿⢹⣿⣿⣿⣿⡟⠁
        ⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋
            ⠙⢿⣿⣿⣿⣿⡿⠏
               ⡀⡁
EOF

def show_banner
  puts "\e[1;31m#{BANNER}\e[0m"
  puts "\e[1;36m═══════════════════════════════════════════════════════════\e[0m"
  puts "\e[1;32m  SocMint-Framework v1.0  ::  Social Media Recon Suite\e[0m"
  puts "\e[1;33m  Author : Mr Sabaz Ali Khan (Cyber Security Engineer)\e[0m"
  puts "\e[1;33m  YouTube | GitHub | LinkedIn : Mr Sabaz Ali Khan\e[0m"
  puts "\e[1;31m  USAGE: Authorized security testing & OSINT only\e[0m"
  puts "\e[1;36m═══════════════════════════════════════════════════════════\e[0m\n\n"
end

# ---------------- COLORS ----------------
def red(s);    "\e[1;31m#{s}\e[0m"; end
def green(s);  "\e[1;32m#{s}\e[0m"; end
def yellow(s); "\e[1;33m#{s}\e[0m"; end
def cyan(s);   "\e[1;36m#{s}\e[0m"; end
def info(s);   puts "[\e[1;34m*\e[0m] #{s}"; end
def ok(s);     puts "[#{green('+')}] #{s}"; end
def warn(s);   puts "[#{yellow('!')}] #{s}"; end
def err(s);    puts "[#{red('x')}] #{s}"; end

# ---------------- TARGET MODULES ----------------
# Each module: URL template + detection logic (public endpoints only)
PLATFORMS = {
  "github"   => { url: "https://github.com/%s",           exists: ->(c,b){ c == 200 } },
  "twitter"  => { url: "https://x.com/%s",                exists: ->(c,b){ c == 200 && !b.include?("page doesn’t exist") } },
  "instagram"=> { url: "https://www.instagram.com/%s/",   exists: ->(c,b){ c == 200 && b.include?('"ProfilePage"') } },
  "reddit"   => { url: "https://www.reddit.com/user/%s/about.json", exists: ->(c,b){ c == 200 && begin JSON.parse(b)["data"].any? rescue false end } },
  "tiktok"   => { url: "https://www.tiktok.com/@%s",      exists: ->(c,b){ c == 200 && !b.include?("Couldn't find this account") } },
  "telegram" => { url: "https://t.me/%s",                 exists: ->(c,b){ c == 200 && !b.include?("tgme_page_not_found") } },
  "medium"   => { url: "https://medium.com/@%s",          exists: ->(c,b){ c == 200 && !b.include?("404") } },
  "pinterest"=> { url: "https://www.pinterest.com/%s/",   exists: ->(c,b){ c == 200 && !b.include?("not found") } },
  "youtube"  => { url: "https://www.youtube.com/@%s",     exists: ->(c,b){ c == 200 && b.include?("Channel") || b.include?("channel") } },
  "vk"       => { url: "https://vk.com/%s",               exists: ->(c,b){ c == 200 && !b.include?("page deleted") && !b.include?("page not found") } }
}

def fetch(url, headers = {})
  uri = URI(url)
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.open_timeout = 8
  http.read_timeout = 8
  req = Net::HTTP::Get.new(uri.request_uri, {
    "User-Agent" => "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
  }.merge(headers))
  res = http.request(req)
  [res.code.to_i, res.body.to_s]
rescue => e
  [0, e.message]
end

# ---------------- MODULE: Username Enumeration ----------------
def enum_usernames(username, results)
  info "Enumerating username '#{cyan(username)}' across #{PLATFORMS.size} platforms..."
  PLATFORMS.each do |name, m|
    url = format(m[:url], URI.encode_www_form_component(username))
    code, body = fetch(url)
    found = m[:exists].call(code, body)
    if code == 0
      warn "#{name.ljust(12)} => unreachable (#{body[0, 60]})"
      results[name] = { status: "error", url: url }
    elsif found
      ok "#{name.ljust(12)} => FOUND  #{url}"
      results[name] = { status: "found", url: url }
    else
      puts "  [ ] #{name.ljust(12)} => not found"
      results[name] = { status: "not_found", url: url }
    end
    sleep(0.3) # be polite, avoid rate limits
  end
end

# ---------------- MODULE: Profile Data (GitHub public API) ----------------
def github_profile(username, results)
  info "Pulling public GitHub profile data..."
  code, body = fetch("https://api.github.com/users/#{username}")
  if code == 200
    d = JSON.parse(body)
    profile = {
      "name"     => d["name"],
      "bio"      => d["bio"],
      "company"  => d["company"],
      "location" => d["location"],
      "email"    => d["email"],
      "followers"=> d["followers"],
      "repos"    => d["public_repos"],
      "created"  => d["created_at"]
    }
    profile.each { |k, v| ok "#{k.ljust(10)}: #{v || 'n/a'}" }
    results["github_data"] = profile
  else
    warn "No public GitHub data for '#{username}'"
  end
end

# ---------------- MODULE: Username Variants ----------------
def variants(username)
  base = username.downcase.gsub(/[^a-z0-9_]/, "")
  v = [base, "_#{base}", "#{base}_", "#{base}1", "#{base}01", "#{base}x"]
  v.uniq
end

# ---------------- MODULE: Breach-Style Email Pattern (public OSINT) ----------------
def email_patterns(username, domain)
  info "Generating likely email patterns (for authorized phishing-sim scoping)..."
  pats = ["#{username}@#{domain}", "#{username}.#{username}@#{domain}",
          "#{username[0]}#{username}@#{domain}", "#{username}@gmail.com"]
  pats.each { |p| puts "  -> #{cyan(p)}" }
  pats
end

# ---------------- REPORT ----------------
def save_report(results, target)
  fname = "report_#{target}_#{Time.now.to_i}.json"
  File.write(fname, JSON.pretty_generate(results))
  ok "Report saved => #{fname}"
end

# ---------------- CLI ----------------
def menu
  puts cyan("  [1] Username enumeration across platforms")
  puts cyan("  [2] Full recon (enum + GitHub data + variants)")
  puts cyan("  [3] Username variant sweep")
  puts cyan("  [4] Email pattern generator")
  puts cyan("  [5] Save last results")
  puts cyan("  [0] Exit")
end

def main
  show_banner
  results = {}
  loop do
    print yellow("\nsocmint> ")
    menu
    print yellow("\nchoice> ")
    case STDIN.gets.strip
    when "1"
      print "username> "; u = STDIN.gets.strip
      next if u.empty?
      enum_usernames(u, results)
    when "2"
      print "username> "; u = STDIN.gets.strip
      next if u.empty?
      enum_usernames(u, results)
      github_profile(u, results)
      puts green("Variants found: #{variants(u).join(', ')}")
    when "3"
      print "username> "; u = STDIN.gets.strip
      v = variants(u)
      v.each do |alt|
        puts "\n#{cyan('>> variant:')} #{alt}"
        enum_usernames(alt, results)
      end
    when "4"
      print "username> "; u = STDIN.gets.strip
      print "target domain> "; d = STDIN.gets.strip
      results["email_patterns"] = email_patterns(u, d)
    when "5"
      save_report(results, "session")
    when "0"
      puts green("\n[+] Exiting. — Mr Sabaz Ali Khan\n")
      break
    else
      err "Invalid option."
    end
  end
end

main if __FILE__ == $0
