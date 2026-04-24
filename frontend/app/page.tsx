'use client'

import Link from 'next/link'
import { motion } from 'framer-motion'
import { 
  FilmIcon, 
  DocumentTextIcon, 
  PhotoIcon, 
  MicrophoneIcon,
  VideoCameraIcon,
  SparklesIcon,
  RocketLaunchIcon
} from '@heroicons/react/24/outline'

export default function Home() {
  const features = [
    {
      name: 'AI Scriptwriting',
      description: 'Generate professional scripts using advanced AI',
      icon: DocumentTextIcon,
      gradient: 'from-blue-500 to-cyan-500',
      href: '/scripts'
    },
    {
      name: 'Storyboarding',
      description: 'Visualize your story with AI-generated storyboards',
      icon: PhotoIcon,
      gradient: 'from-purple-500 to-pink-500',
      href: '/storyboards'
    },
    {
      name: 'Scene Generation',
      description: 'Create stunning video scenes with AI',
      icon: VideoCameraIcon,
      gradient: 'from-orange-500 to-red-500',
      href: '/scenes'
    },
    {
      name: 'AI Voiceovers',
      description: 'Professional voice narration in multiple languages',
      icon: MicrophoneIcon,
      gradient: 'from-green-500 to-emerald-500',
      href: '/voiceovers'
    },
  ]

  return (
    <main className="min-h-screen bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-gray-900 via-gray-900 to-black relative overflow-hidden">
      {/* Animated background orbs */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-purple-600/20 rounded-full blur-3xl animate-pulse"></div>
        <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-blue-600/20 rounded-full blur-3xl animate-pulse delay-1000"></div>
      </div>

      {/* Header */}
      <header className="relative container mx-auto px-4 py-6 backdrop-blur-sm">
        <nav className="flex items-center justify-between">
          <div className="flex items-center space-x-3 group">
            <div className="relative">
              <FilmIcon className="h-8 w-8 text-purple-400 group-hover:text-purple-300 transition-colors" />
              <div className="absolute inset-0 blur-lg bg-purple-400/50 group-hover:bg-purple-300/50 transition-all"></div>
            </div>
            <h1 className="text-2xl font-bold bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
              AI Film Studio
            </h1>
          </div>
          <Link 
            href="/projects" 
            className="group relative px-6 py-2.5 bg-gradient-to-r from-purple-600 to-blue-600 text-white rounded-lg overflow-hidden transition-all hover:shadow-lg hover:shadow-purple-500/50"
          >
            <span className="relative z-10 flex items-center gap-2">
              Get Started
              <RocketLaunchIcon className="h-4 w-4 group-hover:translate-x-1 transition-transform" />
            </span>
            <div className="absolute inset-0 bg-gradient-to-r from-purple-500 to-blue-500 opacity-0 group-hover:opacity-100 transition-opacity"></div>
          </Link>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="relative container mx-auto px-4 py-20 text-center">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="relative"
        >
          <div className="inline-flex items-center gap-2 px-4 py-2 mb-6 bg-purple-500/10 border border-purple-500/20 rounded-full backdrop-blur-sm">
            <SparklesIcon className="h-4 w-4 text-purple-400" />
            <span className="text-sm text-purple-300">Powered by cutting-edge AI</span>
          </div>
          
          <h2 className="text-5xl md:text-7xl font-bold mb-6 leading-tight">
            <span className="bg-gradient-to-r from-white via-gray-100 to-gray-300 bg-clip-text text-transparent">
              Create Professional Videos
            </span>
            <br />
            <span className="bg-gradient-to-r from-purple-400 via-pink-400 to-blue-400 bg-clip-text text-transparent animate-gradient">
              Powered by AI
            </span>
          </h2>
          
          <p className="text-xl text-gray-400 mb-10 max-w-2xl mx-auto leading-relaxed">
            From script to screen in minutes. Automate your entire video production 
            workflow with cutting-edge AI technology.
          </p>
          
          <Link 
            href="/projects/new" 
            className="group relative inline-flex items-center gap-3 px-8 py-4 bg-gradient-to-r from-purple-600 via-pink-600 to-blue-600 text-white text-lg font-semibold rounded-xl overflow-hidden transition-all hover:shadow-2xl hover:shadow-purple-500/50 hover:scale-105"
          >
            <span className="relative z-10">Start Your First Project</span>
            <RocketLaunchIcon className="relative z-10 h-5 w-5 group-hover:translate-x-1 transition-transform" />
            <div className="absolute inset-0 bg-gradient-to-r from-purple-500 via-pink-500 to-blue-500 opacity-0 group-hover:opacity-100 transition-opacity"></div>
            <div className="absolute inset-0 bg-white/20 blur-xl opacity-0 group-hover:opacity-100 transition-opacity"></div>
          </Link>
        </motion.div>
      </section>

      {/* Features Grid */}
      <section className="relative container mx-auto px-4 py-20">
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.3 }}
          className="text-center mb-16"
        >
          <h3 className="text-3xl md:text-4xl font-bold bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent mb-4">
            Everything you need to create amazing videos
          </h3>
          <p className="text-gray-400 text-lg">Powered by the latest AI models and tools</p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((feature, index) => (
            <motion.div
              key={feature.name}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              className="group relative"
            >
              {/* Glow effect */}
              <div className={`absolute -inset-0.5 bg-gradient-to-r ${feature.gradient} rounded-2xl blur opacity-0 group-hover:opacity-75 transition duration-500`}></div>
              
              {/* Card */}
              <div className="relative bg-gray-900/90 backdrop-blur-xl border border-gray-800 rounded-2xl p-8 hover:border-gray-700 transition-all duration-300 h-full">
                {/* Icon with gradient background */}
                <div className={`inline-flex p-3 mb-6 bg-gradient-to-r ${feature.gradient} rounded-xl shadow-lg`}>
                  <feature.icon className="h-8 w-8 text-white" />
                </div>
                
                <h3 className="text-xl font-bold text-white mb-3 group-hover:bg-gradient-to-r group-hover:from-white group-hover:to-gray-300 group-hover:bg-clip-text group-hover:text-transparent transition-all">
                  {feature.name}
                </h3>
                
                <p className="text-gray-400 leading-relaxed mb-6">
                  {feature.description}
                </p>
                
                <Link 
                  href={feature.href}
                  className={`inline-flex items-center gap-2 text-sm font-medium bg-gradient-to-r ${feature.gradient} bg-clip-text text-transparent opacity-0 group-hover:opacity-100 transition-opacity`}
                >
                  Learn more
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                  </svg>
                </Link>
              </div>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="relative container mx-auto px-4 py-12 text-center border-t border-gray-800/50">
        <p className="text-gray-500">&copy; 2026 AI Film Studio. All rights reserved.</p>
      </footer>
    </main>
  )
}
